SELECT 1 + 2, NULL, col1::INT, a <> b, TRUE, false WHERE a = b;
CREATE TABLE foo(a TEXT DEFAULT 'foo');
CREATE TYPE foo AS (a TEXT, b TEXT);
CREATE DOMAIN foo AS TEXT;
