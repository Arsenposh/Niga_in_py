CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM better_phonebook WHERE name = p_name) THEN
        UPDATE better_phonebook SET phonenumber = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO better_phonebook(name, phonenumber) VALUES(p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_search_term VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM better_phonebook WHERE name = p_search_term OR phonenumber = p_search_term) THEN
        DELETE FROM better_phonebook WHERE name = p_search_term OR phonenumber = p_search_term;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_insert(p_name VARCHAR[], p_phonenumber VARCHAR[], INOUT p_errors VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    p_errors = '{}';
    BEGIN
        FOR i in 1..ARRAY_LENGTH(p_name, 1) LOOP
            IF p_phonenumber[i] LIKE '+77_________' THEN
                INSERT INTO better_phonebook(name, phonenumber) VALUES(p_name[i], p_phonenumber[i]);
            ELSE
                p_errors := ARRAY_APPEND(p_errors, p_name[i] || ' ' || p_phonenumber[i]);
            END IF;
        END LOOP;
END;
END;
$$;

