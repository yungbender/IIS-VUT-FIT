INSERT INTO client(clientname, mail, password, name, surname, birth) VALUES ('mirovanco', 'mirovanco@fabus.sk', 'klobasa', 'Miroslav', 'Vanco', '01-01-1998');
INSERT INTO client(clientname, mail, password, name, surname, birth) VALUES ('stepankrobot', 'stepan@svoboda.cz', 'anez', 'Stepan', 'Krobot', '01-01-1998');

INSERT INTO product(name, description, completion_date, version, manager_id) VALUES ('Urychlovac castic', 'super duper urychlovac', '01-01-2025', '1.0', 'stepankrobot');

INSERT INTO product_customer(customer_id, product_id) VALUES ('mirovanco', 'Urychlovac castic');
INSERT INTO product_customer(customer_id, product_id) VALUES ('mirovanco', 'Urychlovac castic');

INSERT INTO ticket(name, description, author_id, product_name) VALUES ('Nefunguje urychlovac', 'Nejde urychlovac ked do neho dam klobasu.', 'mirovanco', 'Urychlovac castic');

INSERT INTO comment(content, ticket_id, author_id) VALUES ('Pracujem na tom sefe.', 1, 'stepankrobot');

