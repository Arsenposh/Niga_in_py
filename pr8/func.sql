CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p TEXT)
RETURNS TABLE(id INT, name VARCHAR, phonenumber VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT * FROM better_phonebook
                 WHERE better_phonebook.name ILIKE '%' || p || '%'
                    OR better_phonebook.phonenumber ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION pagination(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phonenumber VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT * FROM better_phonebook
    ORDER BY name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;