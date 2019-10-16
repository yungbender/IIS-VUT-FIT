CREATE TABLE position
(
    id INTEGER PRIMARY KEY,
    position VARCHAR(64) NOT NULL
);


CREATE TABLE client
(
    clientname VARCHAR(64) PRIMARY KEY,
    mail VARCHAR(64) NOT NULL,
    password VARCHAR(128) NOT NULL,
    name VARCHAR(64),
    surname VARCHAR(64),
    birth DATE,
    image VARCHAR(64) NOT NULL DEFAULT 'default',
    position_id INTEGER NOT NULL REFERENCES position(id) DEFAULT 0,
    work_time INTEGER DEFAULT 0
);

CREATE TABLE task
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(64) NOT NULL,
    description TEXT,
    completion_date TIMESTAMP,
    state SMALLINT NOT NULL DEFAULT 0,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    worker_id VARCHAR(64) REFERENCES client(clientname),
    creator_id VARCHAR(64) REFERENCES client(clientname)
);

CREATE TABLE product
(
    name VARCHAR(64) PRIMARY KEY,
    description TEXT,
    image VARCHAR(64) DEFAULT 'default',
    creation_date DATE DEFAULT CURRENT_DATE,
    completion_date DATE,
    version VARCHAR(64),
    manager_id VARCHAR(64) REFERENCES client(clientname)
);

CREATE TABLE ticket
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    description TEXT NOT NULL,
    state SMALLINT NOT NULL DEFAULT 0,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(64),
    author_id VARCHAR(64) REFERENCES client(clientname),
    product_name VARCHAR(64) REFERENCES product(name)
);

CREATE TABLE comment
(
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    image VARCHAR(64),
    ticket_id SERIAL REFERENCES ticket(id),
    author_id VARCHAR(64) REFERENCES client(clientname)
);

CREATE TABLE task_ticket
(
    task_id SERIAL REFERENCES task(id),
    ticket_id SERIAL REFERENCES ticket(id)
);

CREATE TABLE developer_product
(
    developer_id VARCHAR(64) NOT NULL REFERENCES client(clientname),
    product_id VARCHAR(64) NOT NULL REFERENCES product(name)
);

INSERT INTO position VALUES (0, 'customer');
INSERT INTO position VALUES (1, 'developer');
INSERT INTO position VALUES (2, 'manager');
INSERT INTO position VALUES (3, 'owner');
INSERT INTO position VALUES (4, 'admin');

CREATE USER iis_webapp WITH ENCRYPTED PASSWORD 'iis_passwd';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO iis_webapp;
