<?php
/**
 * Stakeholder Survey Submission Endpoint
 * POST /survey/api/submit.php
 */

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed. Use POST.'], JSON_UNESCAPED_UNICODE);
    exit;
}

require_once __DIR__ . '/db.php';

// Read JSON input
$input_raw = file_get_contents('php://input');
$data = json_decode($input_raw, true);

if (!$data) {
    // Check $_POST if sent via standard form-data
    $data = $_POST;
}

if (empty($data)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'No data received.'], JSON_UNESCAPED_UNICODE);
    exit;
}

// Basic validation for mandatory fields
$required_fields = ['q1_stakeholder_group', 'q2_field', 'q3_tech_relation', 'q4_knowledge', 'q5_special_knowledge', 'q6_skills', 'q7_learning_model', 'q8_ethics', 'q9_character', 'q10_expectations', 'q11_revision_focus', 'q15_top3_priorities', 'q16_graduate_profile'];

$missing = [];
foreach ($required_fields as $field) {
    if (!isset($data[$field]) || trim($data[$field]) === '') {
        $missing[] = $field;
    }
}

if (!empty($missing)) {
    http_response_code(422);
    echo json_encode([
        'success' => false,
        'error' => 'Missing required questions: ' . implode(', ', $missing)
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

// Prepare data
$ip = $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';
$ua = $_SERVER['HTTP_USER_AGENT'] ?? 'UNKNOWN';

// If q15 is an array, encode as json/comma string
$q15 = is_array($data['q15_top3_priorities']) ? json_encode($data['q15_top3_priorities'], JSON_UNESCAPED_UNICODE) : (string)$data['q15_top3_priorities'];

try {
    $stmt = $pdo->prepare("
        INSERT INTO stakeholder_surveys (
            ip_address, user_agent,
            q1_stakeholder_group, q1_other,
            q2_field, q2_other,
            q3_tech_relation, q3_other,
            q4_knowledge, q4_other,
            q5_special_knowledge, q5_other,
            q6_skills, q6_other,
            q7_learning_model, q7_other,
            q8_ethics, q8_other,
            q9_character, q9_other,
            q10_expectations, q10_other,
            q11_revision_focus, q11_other,
            q12_specific, q12_other,
            q13_specific, q13_other,
            q14_specific, q14_other,
            q15_top3_priorities,
            q16_graduate_profile, q16_other,
            additional_comments,
            organization_name, respondent_name, respondent_email
        ) VALUES (
            :ip_address, :user_agent,
            :q1_stakeholder_group, :q1_other,
            :q2_field, :q2_other,
            :q3_tech_relation, :q3_other,
            :q4_knowledge, :q4_other,
            :q5_special_knowledge, :q5_other,
            :q6_skills, :q6_other,
            :q7_learning_model, :q7_other,
            :q8_ethics, :q8_other,
            :q9_character, :q9_other,
            :q10_expectations, :q10_other,
            :q11_revision_focus, :q11_other,
            :q12_specific, :q12_other,
            :q13_specific, :q13_other,
            :q14_specific, :q14_other,
            :q15_top3_priorities,
            :q16_graduate_profile, :q16_other,
            :additional_comments,
            :organization_name, :respondent_name, :respondent_email
        )
    ");

    $stmt->execute([
        ':ip_address' => $ip,
        ':user_agent' => $ua,
        ':q1_stakeholder_group' => $data['q1_stakeholder_group'] ?? '',
        ':q1_other' => $data['q1_other'] ?? null,
        ':q2_field' => $data['q2_field'] ?? '',
        ':q2_other' => $data['q2_other'] ?? null,
        ':q3_tech_relation' => $data['q3_tech_relation'] ?? '',
        ':q3_other' => $data['q3_other'] ?? null,
        ':q4_knowledge' => $data['q4_knowledge'] ?? '',
        ':q4_other' => $data['q4_other'] ?? null,
        ':q5_special_knowledge' => $data['q5_special_knowledge'] ?? '',
        ':q5_other' => $data['q5_other'] ?? null,
        ':q6_skills' => $data['q6_skills'] ?? '',
        ':q6_other' => $data['q6_other'] ?? null,
        ':q7_learning_model' => $data['q7_learning_model'] ?? '',
        ':q7_other' => $data['q7_other'] ?? null,
        ':q8_ethics' => $data['q8_ethics'] ?? '',
        ':q8_other' => $data['q8_other'] ?? null,
        ':q9_character' => $data['q9_character'] ?? '',
        ':q9_other' => $data['q9_other'] ?? null,
        ':q10_expectations' => $data['q10_expectations'] ?? '',
        ':q10_other' => $data['q10_other'] ?? null,
        ':q11_revision_focus' => $data['q11_revision_focus'] ?? '',
        ':q11_other' => $data['q11_other'] ?? null,
        ':q12_specific' => $data['q12_specific'] ?? null,
        ':q12_other' => $data['q12_other'] ?? null,
        ':q13_specific' => $data['q13_specific'] ?? null,
        ':q13_other' => $data['q13_other'] ?? null,
        ':q14_specific' => $data['q14_specific'] ?? null,
        ':q14_other' => $data['q14_other'] ?? null,
        ':q15_top3_priorities' => $q15,
        ':q16_graduate_profile' => $data['q16_graduate_profile'] ?? '',
        ':q16_other' => $data['q16_other'] ?? null,
        ':additional_comments' => $data['additional_comments'] ?? null,
        ':organization_name' => $data['organization_name'] ?? null,
        ':respondent_name' => $data['respondent_name'] ?? null,
        ':respondent_email' => $data['respondent_email'] ?? null,
    ]);

    $inserted_id = $pdo->lastInsertId();

    echo json_encode([
        'success' => true,
        'message' => 'บันทึกข้อมูลแบบสำรวจสำเร็จ ขอขอบพระคุณเป็นอย่างสูงสำหรับข้อมูลอันทรงคุณค่า',
        'survey_id' => $inserted_id,
        'timestamp' => date('Y-m-d H:i:s')
    ], JSON_UNESCAPED_UNICODE);

} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Database write error: ' . $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
}
