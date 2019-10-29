-- Delete previous database and initialize new one
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
DROP ROLE IF EXISTS iis_webapp;

CREATE TABLE position
(
    id INTEGER PRIMARY KEY,
    position VARCHAR(64) NOT NULL
);


CREATE TABLE client
(
    id SERIAL PRIMARY KEY,
    clientname VARCHAR(64) UNIQUE,
    mail VARCHAR(64) NOT NULL,
    password VARCHAR(128) NOT NULL,
    name VARCHAR(64),
    surname VARCHAR(64),
    birth DATE,
    image VARCHAR(64) NOT NULL DEFAULT '1.jpg',
    position_id INTEGER NOT NULL REFERENCES position(id) DEFAULT 0,
    work_time INTEGER DEFAULT 0
);


CREATE TABLE task_state
(
    id SERIAL PRIMARY KEY,
    state VARCHAR(64) NOT NULL
);

CREATE TABLE task
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(64) NOT NULL,
    description TEXT,
    completion_date VARCHAR(64) DEFAULT 'TBA',
    state_id INTEGER NOT NULL DEFAULT 1 REFERENCES task_state(id),
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    worker_id INTEGER REFERENCES client(id),
    creator_id INTEGER REFERENCES client(id)
);

CREATE TABLE product
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(64),
    description TEXT,
    image VARCHAR(64) NOT NULL DEFAULT '2.jpg',
    creation_date DATE DEFAULT CURRENT_DATE,
    completion_date VARCHAR(64),
    version VARCHAR(64),
    manager_id INTEGER REFERENCES client(id)
);

CREATE TABLE ticket
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    description TEXT NOT NULL,
    closed BOOL NOT NULL DEFAULT false,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(64),
    author_id INTEGER REFERENCES client(id),
    product_id INTEGER REFERENCES product(id)
);


CREATE TABLE comment
(
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    image VARCHAR(64),
    ticket_id INTEGER REFERENCES ticket(id),
    task_id INTEGER REFERENCES task(id),
    author_id INTEGER REFERENCES client(id)
);

CREATE TABLE task_ticket
(
    task_id INTEGER REFERENCES task(id),
    ticket_id INTEGER REFERENCES ticket(id)
);

-- Create positions
INSERT INTO position VALUES (0, 'customer');
INSERT INTO position VALUES (1, 'developer');
INSERT INTO position VALUES (2, 'manager');
INSERT INTO position VALUES (3, 'owner');
INSERT INTO position VALUES (4, 'admin');

-- Create task
INSERT INTO task_state VALUES (1, 'SPECIFIED');
INSERT INTO task_state VALUES (2, 'IN PROGRESS');
INSERT INTO task_state VALUES (3, 'ON TESTING');
INSERT INTO task_state VALUES (4, 'DONE');

-- Create webapp account for admin because someone has to be first admin
-- Username: admin, Password: adminananas
INSERT INTO client (clientname, mail, password, name, surname, birth, position_id) 
VALUES ('admin', 'admin@admin.com', 'ccd95ba02a8fde0c44da61e0b96771e9194bfe914c479313b3c5260ba6c80fb50882f9698ff1d1009ba8b690364fb95b12e320c8c3e497d297e532dcbd9e8dfd', 'admin', 'ananas', CURRENT_TIMESTAMP, 4);
INSERT INTO client (clientname, mail, password, name, surname, birth, position_id) 
VALUES ('owner', 'owner@owner.com', 'b8f4f2ab6bd0553667fde56ac3af8acdb72fc8c5907331444112cf3fbc5023ec7cba20d835e76e9bfdb7067083518dfa7693fb6c2f15481f818168daf5e3009d', 'owner', 'ananas', CURRENT_TIMESTAMP, 3);
INSERT INTO client (clientname, mail, password, name, surname, birth, position_id) 
VALUES ('manager', 'manager@manager.com', 'cae12350c78a0286469d505800a02243b3e6bb9845e2b631fe553669a6ba9900dc79aaee7574afd1203110f775bcdff203789bde5130da4694fa3934823f199a', 'manager', 'ananas', CURRENT_TIMESTAMP, 2);
INSERT INTO client (clientname, mail, password, name, surname, birth, position_id) 
VALUES ('developer', 'developer@developer.com', 'c8c4a6fab60b52a0f8c6e7ea6f122aab50191f2104535a1daf4b7546db01b73033e10941ccf3e20a3b578175ed443643dcda723becd7d3d0bc8eaa246176442c', 'developer', 'ananas', CURRENT_TIMESTAMP, 1);


-- Create DB account for webapp to select, delete, etc
CREATE USER iis_webapp WITH ENCRYPTED PASSWORD 'iis_passwd';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO iis_webapp;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO iis_webapp;
