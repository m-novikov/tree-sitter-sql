-- PROCEDURE: public.Proc1_$%{}[]()&*^!@"'`\/#(integer)

-- DROP PROCEDURE IF EXISTS public."Proc1_$%{}[]()&*^!@""'`\/#"(integer);

CREATE OR REPLACE PROCEDURE public."Proc1_$%{}[]()&*^!@""'`\/#"(
	i1 integer)
LANGUAGE 'plpgsql'
AS $BODY$
begin
select 1;
end;
$BODY$;

ALTER PROCEDURE public."Proc1_$%{}[]()&*^!@""'`\/#"(integer)
    OWNER TO postgres;
