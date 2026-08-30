<?php
/**
 * Stakeholder Survey Database Handler
 * M.Eng. Computer Engineering & Artificial Intelligence (CPE & AI)
 * Uttaradit Rajabhat University
 * Supports SQLite (Default, zero setup) & MySQL / MariaDB (via environment/config)
 */

$db_type = getenv('DB_TYPE') ?: 'sqlite';
$data_dir = __DIR__ . '/../data';

if (!file_exists($data_dir)) {
    @mkdir($data_dir, 0777, true);
}

$pdo = null;

try {
    if ($db_type === 'mysql') {
        $host = getenv('DB_HOST') ?: '127.0.0.1';
        $port = getenv('DB_PORT') ?: '3306';
        $dbname = getenv('DB_NAME') ?: 'cpe_ai_survey';
        $user = getenv('DB_USER') ?: 'root';
        $pass = getenv('DB_PASS') ?: '';
        
        $dsn = "mysql:host={$host};port={$port};dbname={$dbname};charset=utf8mb4";
        $pdo = new PDO($dsn, $user, $pass, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
    } else {
        // SQLite
        $sqlite_file = $data_dir . '/survey.db';
        $pdo = new PDO("sqlite:" . $sqlite_file);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        $pdo->exec("PRAGMA journal_mode = WAL;");
    }

    // Auto-create table schema if not exists
    $schema_sql = "
    CREATE TABLE IF NOT EXISTS stakeholder_surveys (
        id INTEGER PRIMARY KEY " . ($db_type === 'mysql' ? 'AUTO_INCREMENT' : 'AUTOINCREMENT') . ",
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ip_address VARCHAR(45) NULL,
        user_agent TEXT NULL,
        
        -- Section 1: General Info
        q1_stakeholder_group VARCHAR(100) NOT NULL,
        q1_other TEXT NULL,
        q2_field VARCHAR(100) NOT NULL,
        q2_other TEXT NULL,
        q3_tech_relation VARCHAR(100) NOT NULL,
        q3_other TEXT NULL,
        
        -- Section 2: OBE Competencies
        q4_knowledge VARCHAR(150) NOT NULL,
        q4_other TEXT NULL,
        q5_special_knowledge VARCHAR(150) NOT NULL,
        q5_other TEXT NULL,
        q6_skills VARCHAR(150) NOT NULL,
        q6_other TEXT NULL,
        q7_learning_model VARCHAR(150) NOT NULL,
        q7_other TEXT NULL,
        q8_ethics VARCHAR(150) NOT NULL,
        q8_other TEXT NULL,
        q9_character VARCHAR(150) NOT NULL,
        q9_other TEXT NULL,
        
        -- Section 3: Expectations
        q10_expectations VARCHAR(150) NOT NULL,
        q10_other TEXT NULL,
        q11_revision_focus VARCHAR(150) NOT NULL,
        q11_other TEXT NULL,
        
        -- Section 4: Specific Group Branching
        q12_specific VARCHAR(150) NULL,
        q12_other TEXT NULL,
        q13_specific VARCHAR(150) NULL,
        q13_other TEXT NULL,
        q14_specific VARCHAR(150) NULL,
        q14_other TEXT NULL,
        
        -- Section 5: Summary
        q15_top3_priorities TEXT NOT NULL,
        q16_graduate_profile VARCHAR(150) NOT NULL,
        q16_other TEXT NULL,
        
        -- Additional Comments
        additional_comments TEXT NULL,
        organization_name VARCHAR(255) NULL,
        respondent_name VARCHAR(255) NULL,
        respondent_email VARCHAR(255) NULL
    );";

    $pdo->exec($schema_sql);

} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Database connection failed: ' . $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
    exit;
}
