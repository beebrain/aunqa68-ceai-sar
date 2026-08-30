<?php
/**
 * Stakeholder Survey Analytics Endpoint
 * GET /survey/api/analytics.php
 */

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/db.php';

try {
    $filter_group = $_GET['group'] ?? null;
    $where_sql = "";
    $params = [];

    if ($filter_group && $filter_group !== 'all') {
        $where_sql = " WHERE q1_stakeholder_group = :grp";
        $params[':grp'] = $filter_group;
    }

    // Total count
    $stmt = $pdo->prepare("SELECT COUNT(*) as total FROM stakeholder_surveys" . $where_sql);
    $stmt->execute($params);
    $total_responses = (int)$stmt->fetch()['total'];

    // Group breakdown
    $stmt = $pdo->query("SELECT q1_stakeholder_group as `group`, COUNT(*) as `count` FROM stakeholder_surveys GROUP BY q1_stakeholder_group ORDER BY `count` DESC");
    $groups = $stmt->fetchAll();

    // Helper for single choice distribution
    function getDistribution($pdo, $column, $where_sql, $params) {
        $stmt = $pdo->prepare("SELECT {$column} as `value`, COUNT(*) as `count` FROM stakeholder_surveys {$where_sql} GROUP BY {$column} ORDER BY `count` DESC");
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    // Distribution for key OBE domains
    $analytics = [
        'total' => $total_responses,
        'groups_breakdown' => $groups,
        'q1_stakeholders' => getDistribution($pdo, 'q1_stakeholder_group', $where_sql, $params),
        'q2_fields' => getDistribution($pdo, 'q2_field', $where_sql, $params),
        'q3_tech_relation' => getDistribution($pdo, 'q3_tech_relation', $where_sql, $params),
        'q4_knowledge' => getDistribution($pdo, 'q4_knowledge', $where_sql, $params),
        'q5_special_knowledge' => getDistribution($pdo, 'q5_special_knowledge', $where_sql, $params),
        'q6_skills' => getDistribution($pdo, 'q6_skills', $where_sql, $params),
        'q7_learning_model' => getDistribution($pdo, 'q7_learning_model', $where_sql, $params),
        'q8_ethics' => getDistribution($pdo, 'q8_ethics', $where_sql, $params),
        'q9_character' => getDistribution($pdo, 'q9_character', $where_sql, $params),
        'q10_expectations' => getDistribution($pdo, 'q10_expectations', $where_sql, $params),
        'q11_revision_focus' => getDistribution($pdo, 'q11_revision_focus', $where_sql, $params),
        'q16_graduate_profile' => getDistribution($pdo, 'q16_graduate_profile', $where_sql, $params),
    ];

    // Q15 Top 3 checkboxes aggregate
    $stmt = $pdo->prepare("SELECT q15_top3_priorities FROM stakeholder_surveys" . $where_sql);
    $stmt->execute($params);
    $q15_rows = $stmt->fetchAll(PDO::FETCH_COLUMN);

    $q15_counts = [];
    foreach ($q15_rows as $row) {
        $decoded = json_decode($row, true);
        if (is_array($decoded)) {
            foreach ($decoded as $item) {
                $q15_counts[$item] = ($q15_counts[$item] ?? 0) + 1;
            }
        } elseif (!empty($row)) {
            $items = explode(',', $row);
            foreach ($items as $item) {
                $item = trim($item);
                if ($item) $q15_counts[$item] = ($q15_counts[$item] ?? 0) + 1;
            }
        }
    }
    arsort($q15_counts);
    $analytics['q15_top3_ranking'] = $q15_counts;

    // Recent 10 comments
    $stmt = $pdo->prepare("SELECT created_at, q1_stakeholder_group, organization_name, additional_comments FROM stakeholder_surveys WHERE additional_comments IS NOT NULL AND additional_comments != '' {$where_sql} ORDER BY id DESC LIMIT 15");
    $stmt->execute($params);
    $analytics['recent_comments'] = $stmt->fetchAll();

    echo json_encode(['success' => true, 'data' => $analytics], JSON_UNESCAPED_UNICODE);

} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => $e->getMessage()], JSON_UNESCAPED_UNICODE);
}
