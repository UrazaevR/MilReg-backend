-- Создание пользовательских доменов (типов) на основе текста
CREATE DOMAIN OKIN_01     AS VARCHAR(256);
CREATE DOMAIN OKIN_02     AS VARCHAR(256);
CREATE DOMAIN OKIN_30     AS VARCHAR(256);
CREATE DOMAIN OKPDTR_CODE AS VARCHAR(256);
CREATE DOMAIN OKIN_10     AS VARCHAR(256);
CREATE DOMAIN OKIN_04     AS VARCHAR(256);
CREATE DOMAIN OKIN_05     AS VARCHAR(256);

-- Таблица подразделений
CREATE TABLE departments (
    id         SERIAL PRIMARY KEY,
    full_name  VARCHAR(256) NOT NULL,   -- полное наименование
    short_name VARCHAR(256) NOT NULL    -- краткое наименование
);

-- Таблица штатного расписания (добавлено поле department_id)
CREATE TABLE staffing_table (
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(256),
    count         INTEGER,
    department_id INTEGER REFERENCES departments (id)
);

-- Таблица сотрудников (ссылается на staffing_table)
CREATE TABLE persons (
    id               SERIAL PRIMARY KEY,
    surname          VARCHAR(256) NOT NULL,
    name             VARCHAR(256) NOT NULL,
    middle_name      VARCHAR(256),
    birth_day        DATE         NOT NULL,
    sex              OKIN_01,
    citizenship      OKIN_02,
    education_level  OKIN_30      NOT NULL,
    main_profession  OKPDTR_CODE,
    other_profession OKPDTR_CODE,
    family_status    OKIN_10,
    inn              VARCHAR(256),
    inn_issue_date   DATE,
    snils            VARCHAR(256),
    snils_issue_date DATE,
    staff_table_id   INTEGER REFERENCES staffing_table (id)
);

-- Таблица водительских удостоверений (с person_id)
CREATE TABLE drivers_licenses (
    id         SERIAL PRIMARY KEY,
    person_id  INTEGER REFERENCES persons (id),
    series     VARCHAR(256),
    number     VARCHAR(256),
    issue_date DATE,
    categories VARCHAR(256)
);

-- Документы об образовании
CREATE TABLE education_docs (
    id           SERIAL PRIMARY KEY,
    person_id    INTEGER REFERENCES persons (id),
    name         VARCHAR(256),
    series       VARCHAR(256),
    number       VARCHAR(256),
    issue_date   DATE,
    organization VARCHAR(256),
    okso_code    VARCHAR(256)
);

-- Знание языков
CREATE TABLE languages (
    id        SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES persons (id),
    language  OKIN_04 NOT NULL,
    knowledge OKIN_05 NOT NULL
);

-- Паспорта
CREATE TABLE passports (
    id           SERIAL PRIMARY KEY,
    person_id    INTEGER REFERENCES persons (id),
    series       VARCHAR(256),
    number       VARCHAR(256),
    issue_date   DATE,
    organization VARCHAR(256),
    code         VARCHAR(256)
);