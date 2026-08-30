<?php
/**
 * Stakeholder Survey Data Export Endpoint
 * GET /survey/api/export.php?format=csv
 */

require_once __DIR__ . '/db.php';

$format = $_GET['format'] ?? 'csv';

try {
    $stmt = $pdo->query("SELECT * FROM stakeholder_surveys ORDER BY id ASC");
    $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if ($format === 'json') {
        header('Content-Type: application/json; charset=utf-8');
        header('Content-Disposition: attachment; filename="cpe_ai_stakeholder_survey_' . date('Ymd_His') . '.json"');
        echo json_encode($rows, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
        exit;
    }

    // Default: CSV Export
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="cpe_ai_stakeholder_survey_' . date('Ymd_His') . '.csv"');

    $output = fopen('php://output', 'w');

    // Add UTF-8 BOM for Microsoft Excel Thai compatibility
    fputs($output, "\xEF\xBB\xBF");

    if (!empty($rows)) {
        // Headers
        $headers = array_keys($rows[0]);
        fputcsv($output, $headers);

        // Data
        foreach ($rows as $row) {
            fputcsv($output, $row);
        }
    } else {
        fputcsv($output, ['id', 'message']);
        fputcsv($output, [1, 'No survey records found.']);
    }

    fclose($output);
    exit;

} catch (Exception $e) {
    http_response_code(500);
    echo "Export Error: " . $e->getMessage();
}
