CREATE FUNCTION something(integer) RETURNS text
AS $somethinghere$select $$hello$$;$somethinghere$
LANGUAGE SQL;

CREATE FUNCTION something(integer) RETURNS integer
    AS $somethinghere$select $1;$somethinghere$
    LANGUAGE SQL;