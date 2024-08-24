Linux: https://www.youtube.com/watch?v=fEGSA68uAR4&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=7
Algorith: https://builtin.com/data-science/tour-top-10-algorithms-machine-learning-newbies

# Why PostgreSQL

## Scalability Battle

It's not about NoSQL vs SQL, it's about BASE vs ACID.

Scalable has to be broken down into its constituents:

Read scaling = handle higher volumes of read operations
Write scaling = handle higher volumes of write operations
ACID-compliant databases (like traditional RDBMS's) can scale reads. They are not inherently less efficient than NoSQL databases because the (possible) performance bottlenecks are introduced by things NoSQL (sometimes) lacks (like joins and where restrictions) which you can opt not to use. Clustered SQL RDBMS's can scale reads by introducing additional nodes in the cluster. There are constraints to how far read operations can be scaled, but these are imposed by the difficulty of scaling up writes as you introduce more nodes into the cluster.

Write scaling is where things get hairy. There are various constraints imposed by the ACID principle which you do not see in eventually-consistent (BASE) architectures:

Atomicity means that transactions must complete or fail as a whole, so a lot of bookkeeping must be done behind the scenes to guarantee this.
Consistency constraints mean that all nodes in the cluster must be identical. If you write to one node, this write must be copied to all other nodes before returning a response to the client. This makes a traditional RDBMS cluster hard to scale.
Durability constraints mean that in order to never lose a write you must ensure that before a response is returned to the client, the write has been flushed to disk.
To scale up write operations or the number of nodes in a cluster beyond a certain point you have to be able to relax some of the ACID requirements:

Dropping Atomicity lets you shorten the duration for which tables (sets of data) are locked. Example: MongoDB, CouchDB.
Dropping Consistency lets you scale up writes across cluster nodes. Examples: riak, cassandra.
Dropping Durability lets you respond to write commands without flushing to disk. Examples: memcache, redis.
NoSQL databases typically follow the BASE model instead of the ACID model. They give up the A, C and/or D requirements, and in return they improve scalability. Some, like Cassandra, let you opt into ACID's guarantees when you need them. However, not all NoSQL databases are more scalable all the time.

The SQL API lacks a mechanism to describe queries where ACID's requirements are relaxed. This is why the BASE databases are all NoSQL.

Personal note: one final point I'd like to make is that most cases where NoSQL is currently being used to improve performance, a solution would be possible on a proper RDBMS by using a correctly normalized schema with proper indexes. As proven by this very site (powered by MS SQL Server) RDBMS's can scale to high workloads, if you use them appropriately. People who don't understand how to optimize RDBMS's should stay away from NoSQL, because they don't understand what risks they are taking with their data.

Update (2019-09-17):

The landscape of databases has evolved since posting this answer. While there is still the dichotomy between the RDBMS ACID world and the NoSQL BASE world, the line has become fuzzier. The NoSQL databases have been adding features from the RDBMS world like SQL API's and transaction support. There are now even databases which promise SQL, ACID and write scaling, like Google Cloud Spanner, YugabyteDB or CockroachDB. Typically the devil is in the details, but for most purposes these are "ACID enough". For a deeper dive into database technology and how it has evolved you can take a look at this slide deck (the slide notes have the accompanying explanation).

_Query Complexity_: Relational databases support complex SQL queries and join operations that span multiple tables. Sharding and partitioning data can introduce additional complexity in query planning and optimization, as queries may need to be distributed and executed across multiple shards or partitions.

_Transaction Management_: Relational databases often rely on centralized transaction management and locking mechanisms to ensure data consistency. Scaling out relational databases can introduce challenges related to distributed transaction coordination, deadlock detection, and concurrency control across multiple nodes.

⚠️ 🔴 ⚠️
While these challenges exist, many relational databases offer features and capabilities to support sharding, partitioning, and scaling out:

Sharding and Partitioning: Relational databases such as MySQL Cluster, PostgreSQL, and Oracle Database offer built-in support for sharding and partitioning through features like MySQL Cluster's NDB Cluster, PostgreSQL's table partitioning, and Oracle Database's partitioning options.

Scaling Out: Relational databases can be scaled out horizontally by deploying multiple database instances or replicas and using techniques like replication, clustering, and load balancing. Technologies like MySQL Group Replication, PostgreSQL streaming replication, and Oracle Real Application Clusters (RAC) enable horizontal scaling of relational databases.

Middleware and Sharding Frameworks: Additionally, there are middleware solutions and sharding frameworks (e.g., Vitess, Citus) specifically designed to facilitate sharding and scaling out of relational databases. These frameworks abstract the complexities of sharding and provide mechanisms for distributing data and queries across multiple nodes.

## Sharding vs scaling vs partitioning

1. Sharding:

Sharding is a technique used to horizontally partition data across multiple databases or servers. Each shard contains a subset of the data.
The goal of sharding is to distribute the load evenly across multiple servers and improve performance and scalability.
Sharding is commonly used in large-scale databases where storing all data on a single server becomes impractical or inefficient.
Sharding typically involves a sharding key, which determines how data is distributed across shards. Different data shards can be located on different physical servers or instances.

2. Scaling:
   Scaling refers to the process of increasing the capacity or capability of a system to handle a growing amount of work or users.
   Scaling can be done either vertically (scaling up) or horizontally (scaling out).
   Vertical scaling involves upgrading the resources of a single server, such as increasing CPU, RAM, or storage capacity.
   Horizontal scaling involves adding more servers or instances to distribute the workload across multiple machines. This can include techniques like sharding.
   The goal of scaling is to maintain performance and availability as the demand for a system grows.

3. Partitioning:
   Partitioning is a technique used to divide a large dataset into smaller, more manageable partitions or segments.
   Unlike sharding, which typically involves distributing data across separate servers, partitioning can be done within a single database or system.
   Partitioning can improve query performance and reduce contention by limiting the amount of data that needs to be accessed or manipulated for a given operation.
   Partitioning can be based on various criteria, such as range partitioning (based on a range of values), hash partitioning (based on a hash function), or list partitioning (based on specific values or conditions).

## Clustering in SQL

Clustering, in the context of databases, refers to a technique used to physically order the rows of a table based on one or more columns. This ordering groups related rows together on disk, typically based on the values of one or more clustering columns. The primary goal of clustering is to improve data access performance by reducing the need for random disk I/O and improving data locality.

Here's how clustering works:

Choice of Clustering Columns: When creating or altering a table, you can specify one or more clustering columns, which determine the order in which rows are physically stored on disk. These columns are often chosen based on the typical access patterns and queries performed on the table.

Sorting and Storing Data: When data is inserted into a clustered table, it is sorted and stored on disk based on the values of the clustering columns. Related rows with similar or adjacent clustering column values are stored together, creating clusters of related data.

Improved Data Access: When querying a clustered table, accessing data based on the clustering columns or a subset of them can benefit from improved data access performance. Because related rows are stored together on disk, accessing data within the same cluster can often be done with sequential scans rather than random disk seeks.

Reduced Disk I/O: Clustering can reduce the need for random disk I/O when accessing related data, as sequential scans within a cluster are typically more efficient than random disk seeks. This can lead to faster query execution times and improved overall system performance.

Data Locality: Clustering improves data locality by storing related data together on disk. This can result in better cache utilization and reduced latency when accessing data, as related data is more likely to be stored in memory or cached.

⚠️ Importantt!!!
It would be a great technicue to combine clustering with indexing.
Why??

Clustering refers to physically ordering the rows of a table based on one or more columns. When combined with indexing, which provides fast lookup of rows based on specific criteria, queries that utilize the indexed columns can benefit from both efficient access to data via the index and improved data locality due to clustering. This can result in faster query execution times.

Remember Clustering can be expensive on write.

## UUIDs are Bad for Performance in MySQL - Is Postgres better? Let us Discuss

https://www.youtube.com/watch?v=Y5mWz4vK10A

## NoSQL VS SQL

PostgreSQL is known as an relational/ SQL data management.

But what is the difference between SQL and NoSQL systems?

- NoSQL systems usually keep data in JSON-like fields. What’s more, any alike files in NoSQL systems can be compiled into collections. These systems accept any type of document.
- SQL systems usually store information in data tables. The tables are interconnected and have a fixed data template. Such strictness seems less attractive, yet it minimizes the possibility of any mistakes.

SQL has some restictions, to start running your project in SQL, you need to design your database prior to any business logic which are the schemas. After you've created your schema, it would be quite hard to implement any changes. In NoSQL there are no shuch restrictions.

- JOIN Clause
  It is another useful feature of SQL. It enables you to retrieve all necessary data from the chosen tables using SQL mechanisms. In NoSQL, there is no such option. Instead, you can extract the required information manually.

- Transactions

Highest integrity and accuracy of your data is of top priority for SQL systems. Another proof of it is their transaction mechanisms. These databases enable placing two or more updates during any transaction. It means that by any transaction, all your updates can either be accepted or fail. In any case, the accuracy of your data will be preserved.

This mechanism doesn’t work for NoSQL databases, where every update is accepted or declined individually. It can lead to pitty consequences: your data can be irrelevant in the end.

- Which one to use??? 😕
  Let’s summarize our points. Again, everything depends on your project. For apps with simple data structure, NoSQL databases are OK. If you’re working with regular apps or middle-size projects, then consider using SQL. Finally, if you’re running super high load projects, you can either use NoSQL or start working with SQL and then migrate to NoSQL.

- Extra informations about V 9.4
  Within its version 9.4, Postgres added some optimizations and updates, but most importantly, it offered HStore and JSONB, a binary version of JSON storage.

Postgres has implemented some NoSQL features, but not all of them. For instance, it lacks `horizontal scaling`. Yet, this implementations still put Postgres in an advantage, since it can combine both ― SQL and NoSQL practices. Thus, you can join NoSQL data with SQL tables. And it will work correctly.

## SQL Battle: PostgreSQL vs MySQL

### Concurrency

Link `Multiversion Concurrency Control`: https://www.youtube.com/watch?v=iM71d2krbS4
The winner here is PostgreSQL. This database handles concurrency much better than its competitor MySQL (see above). It is so thanks to `Multiversion Concurrency Control` which Postgres implements.

### Triggers: PostgreSQL vs MySQL

Postgres supports triggers that can react to most types of command, except for those that affect the database globally e.g., roles and tablespaces. MySQL, in its turn, is limited to only some commands.

- Trigger Example:

```SQL

CREATE TABLE company (
 id SERIAL PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 created_at TIMESTAMP,
 modified_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE log (
 id SERIAL PRIMARY KEY NOT NULL,
 table_name TEXT NOT NULL,
 table_id TEXT NOT NULL,
 description TEXT NOT NULL,
 created_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION add_log_function()
 RETURNS TRIGGER AS $BODY$
DECLARE
 vDescription TEXT;
 vId INT;
 vReturn RECORD;
BEGIN
 vDescription := TG_TABLE_NAME || ' ';
 IF (TG_OP = 'INSERT') THEN
 vId := NEW.id;
 vDescription := vDescription || 'added. Id: ' || vId;
 vReturn := NEW;
 ELSIF (TG_OP = 'UPDATE') THEN
 vId := NEW.id;
 vDescription := vDescription || 'updated. Id: ' || vId;
 vReturn := NEW;
 ELSIF (TG_OP = 'DELETE') THEN
 vId := OLD.id;
 vDescription := vDescription || 'deleted. Id: ' || vId;
 vReturn := OLD;
 END IF;
 RAISE NOTICE 'TRIGER called on % - Log: %', TG_TABLE_NAME, vDescription;
 INSERT INTO log
 (table_name, table_id, description, created_at)
 VALUES
 (TG_TABLE_NAME, vId, vDescription, NOW());
 RETURN vReturn;
END $BODY$
 LANGUAGE plpgsql;

CREATE TRIGGER add_log_trigger
AFTER INSERT OR UPDATE OR DELETE
ON company
FOR EACH ROW
EXECUTE PROCEDURE add_log_function();

INSERT INTO company (NAME) VALUES ('Company 1');
INSERT INTO company (NAME) VALUES ('Company 2');
INSERT INTO company (NAME) VALUES ('Company 3');
UPDATE company SET NAME='Company new 2' WHERE NAME='Company 2';
DELETE FROM company WHERE NAME='Company 1';
SELECT * FROM log;

```

- Basic PL/pgSQL Trigger Function

```SQL

-- Create the trigger function.
CREATE OR REPLACE FUNCTION my_simple_trigger_function()
RETURNS TRIGGER AS
$BODY$
BEGIN
 -- TG_TABLE_NAME :name of the table that caused the trigger invocation
IF (TG_TABLE_NAME = 'users') THEN
 --TG_OP : operation the trigger was fired
 IF (TG_OP = 'INSERT') THEN
 --NEW.id is holding the new database row value (in here id is the id column in users table)
 --NEW will return null for DELETE operations
 INSERT INTO log_table (date_and_time, description) VALUES (NOW(), 'New user inserted. User ID:
'|| NEW.id);
 RETURN NEW;
 ELSIF (TG_OP = 'DELETE') THEN
 --OLD.id is holding the old database row value (in here id is the id column in users table)
 --OLD will return null for INSERT operations
 INSERT INTO log_table (date_and_time, description) VALUES (NOW(), 'User deleted.. User ID: ' ||
OLD.id);
 RETURN OLD;

 END IF;
RETURN NULL;
END IF;
END;
$BODY$
LANGUAGE plpgsql VOLATILE
COST 100;



-- Adding this trigger function to the users table
CREATE TRIGGER my_trigger
AFTER INSERT OR DELETE
ON users
FOR EACH ROW
EXECUTE PROCEDURE my_simple_trigger_function();





```

⚠️⚠️ Key Notes ⚠️⚠️

In PostgreSQL, there are two types of triggers: `row-level triggers` and `statement-level triggers`. These triggers differ in terms of when they are executed and what data they have access to.

1 - Row-Level Triggers:
Row-level triggers are executed once for each row affected by the triggering event. They have access to the individual rows being modified and can reference the OLD and NEW row variables to access the old and new row values, respectively. Row-level triggers are typically used for enforcing complex business rules or performing actions on a per-row basis.

For example, let's say you have a table called employees with columns id, name, and salary. You can create a row-level trigger that automatically updates the last_updated column whenever an employee's salary is changed:

```SQL

CREATE OR REPLACE FUNCTION update_last_updated()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.last_updated = current_timestamp;
    RETURN NEW;
END;
$$;

CREATE TRIGGER salary_trigger
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION update_last_updated();


```

In this example, the update_last_updated function is a row-level trigger function that updates the last_updated column of the NEW row with the current timestamp. The trigger is associated with the BEFORE UPDATE event on the employees table and is executed for each affected row.

2 - Statement-Level Triggers:
Statement-level triggers are executed once for each triggering event, regardless of the number of rows affected. They don't have access to the individual rows being modified, but they can access the OLD and NEW row variables as whole row sets. Statement-level triggers are often used for logging, auditing, or performing actions that are not dependent on specific row values.

Continuing with the employees table example, let's create a statement-level trigger that logs the details of any DELETE statement executed on the table:

```SQL

 CREATE OR REPLACE FUNCTION log_deletes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO delete_log (table_name, deleted_timestamp)
    VALUES (TG_TABLE_NAME, current_timestamp);
    RETURN NULL;
END;
$$;

CREATE TRIGGER delete_trigger
AFTER DELETE ON employees
EXECUTE FUNCTION log_deletes();


```

In this example, the log_deletes function is a statement-level trigger function that inserts a log entry into the delete_log table whenever a DELETE statement is executed on the employees table. The trigger is associated with the AFTER DELETE event and is executed once for each DELETE statement, regardless of the number of rows affected.

To summarize, row-level triggers are executed once for each affected row and have access to individual row values (OLD and NEW), while statement-level triggers are executed once per triggering event and have access to row sets (OLD and NEW). The choice between row-level and statement-level triggers depends on the specific requirements of your application or business logic.

### Event Triggers

Dont confuse triggers whith event triggers because sometimes it gets tricky to seperate their logic, the term "event trigger" specifically refers to triggers that are associated with database events, such as table creation, deletion, or transaction start/end. On the other hand, "trigger" without the term "event" typically refers to the more general concept of triggers in PostgreSQL, which includes both event triggers and traditional triggers associated with table modifications (row-level or statement-level triggers ⬆️).

Here's a breakdown of the difference between the two:

1 - Event Triggers:
Event triggers are specifically designed to respond to specific events occurring within the database. They are associated with event types defined by the database system, such as DDL (Data Definition Language) events, transaction events, or database object events. When the associated event occurs, the event trigger's function is automatically invoked.

Event triggers are useful for implementing custom actions or procedures that need to be triggered by database-level events. For example, you can create an event trigger that sends a notification whenever a new table is created or logs specific DDL commands. Event triggers allow you to extend the functionality of PostgreSQL by responding to database-wide events.

2 - Traditional Triggers:
Traditional triggers, also known as table triggers or data triggers, are associated with modifications (INSERT, UPDATE, DELETE) on specific tables. They can be row-level triggers or statement-level triggers.

Row-level triggers are executed once for each row affected by the triggering event. They can access and manipulate the individual row values being modified. Row-level triggers are commonly used to enforce complex business rules, perform data validation, or maintain data integrity.

Statement-level triggers are executed once per triggering event, regardless of the number of rows affected. They don't have access to individual row values but can work with the whole set of rows being modified. Statement-level triggers are often used for logging, auditing, or performing actions that are not dependent on specific row values.

In summary, "event triggers" specifically refer to triggers associated with database events, while "triggers" generally encompass both event triggers and traditional triggers associated with table modifications.

Examples:

1 - Logging Table Creations:
You can create an event trigger to log whenever a new table is created in the database. This can be useful for tracking schema changes or auditing purposes. Here's an example:

```SQL

CREATE OR REPLACE FUNCTION log_table_creation()
RETURNS event_trigger
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Table % created.', tg_tag;
END;
$$;

CREATE EVENT TRIGGER table_creation_trigger
ON ddl_command_end
EXECUTE FUNCTION log_table_creation();


```

In this example, the log_table_creation function is an event trigger function associated with the ddl_command_end event. When a table is created, the trigger function raises a notice message indicating the table name.

2 - Auditing Database Object Changes:
You can create an event trigger to audit changes to database objects, such as tables, views, or functions. The trigger can capture details of the modification and store them in an audit log table. Here's an example:

```SQL
CREATE OR REPLACE FUNCTION audit_database_objects()
RETURNS event_trigger
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO audit_log (event_type, object_name, modified_timestamp)
    VALUES (tg_tag, TG_TABLE_NAME, current_timestamp);
END;
$$;

CREATE EVENT TRIGGER database_object_trigger
ON ddl_command_end
EXECUTE FUNCTION audit_database_objects();

```

In this example, the audit_database_objects function is an event trigger function associated with the ddl_command_end event. It inserts an entry into the audit_log table whenever a database object is modified, including the event type, object name, and timestamp.

💥 Here is a list of events that you can use with event triggers to capture different types of database activities.

Here is a list of commonly used events:

1. `ddl_command_start`:
   This event occurs before the execution of a DDL (Data Definition Language) command.
2. `ddl_command_end`:
   This event occurs after the execution of a DDL command.
3. `sql_drop`:
   This event occurs when a SQL DROP statement is executed to drop a database object (e.g., table, view, index).
4. `sql_create`:
   This event occurs when a SQL CREATE statement is executed to create a new database object.
5. `sql_alter`:
   This event occurs when a SQL ALTER statement is executed to modify an existing database object.
6. `table_rewrite`:
   This event occurs when a table is rewritten due to a TRUNCATE, ALTER TABLE, or VACUUM FULL operation.
7. `table_scan`:
   This event occurs when a sequential scan of a table is performed.
8. `table_rewrite`:
   This event occurs when a table is rewritten due to a TRUNCATE, ALTER TABLE, or VACUUM FULL operation.
9. `truncate`:
   This event occurs when a table is truncated using the TRUNCATE statement.
10. `database_drop`:
    This event occurs when a database is dropped using the DROP DATABASE statement.

### Procedures

Procedures in PostgreSQL are named blocks of code that encapsulate a series of SQL statements or procedural logic. They are stored in the database and can be invoked by their name to execute the code they contain. Procedures allow you to organize and modularize your code, making it easier to manage and reuse.

By using procedures, you can encapsulate complex logic, ensure code reusability, and improve code organization in your PostgreSQL database. They provide a way to execute a sequence of SQL statements or procedural code as a single unit, making it easier to manage and maintain database operations.

Example:

Let's say you have a database table called "orders" that stores information about customer orders, and you want to create a procedure that calculates the total order value for a given order ID.

```SQL

-- Create the "orders" table:
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);


-- Create the procedure:
CREATE OR REPLACE PROCEDURE calculate_order_total(
    IN order_id INTEGER,
    OUT total DECIMAL(10, 2)
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT SUM(total_amount) INTO total
    FROM orders
    WHERE id = order_id;
END;
$$;


-- Call the procedure:
CALL calculate_order_total(1, total);

```

- Here are a few advanced features and concepts related to procedures in PostgreSQL:

1. Transaction Control: Procedures can participate in transactions and provide control over transaction boundaries. You can use statements like COMMIT, ROLLBACK, and SAVEPOINT within the procedure body to manage transactional behavior.

2. Exception Handling: Procedures can handle exceptions that may occur during their execution. You can use the EXCEPTION block to catch and handle specific errors, or you can let the exception propagate up to the caller. The RAISE statement can be used to raise custom exceptions or re-throw caught exceptions.

3. Dynamic SQL: Procedures can generate and execute dynamic SQL statements using the EXECUTE statement. This allows you to construct SQL statements based on runtime conditions or dynamic input parameters.

4. Cursors: Procedures can use cursors to retrieve and process result sets row by row. Cursors allow you to fetch rows incrementally and perform operations on each row individually.

5. Security and Privileges: Procedures have their own set of permissions and access control rules. You can grant or revoke privileges to execute or modify procedures, ensuring that only authorized users or roles can access them.

6. Function Overloading: PostgreSQL allows you to define multiple procedures with the same name but different parameter signatures, known as function overloading. This allows you to provide different versions of a procedure that can accept different sets of input parameters.

- Here are some common use cases for procedures:

1. Data Validation and Transformation: Procedures are often used to validate and transform incoming data before it is inserted or updated in the database. This can involve checking constraints, performing data conversions, or applying business rules to ensure data integrity.

2. Business Rules and Workflows: Procedures are used to implement and enforce business rules and workflows within a database. This includes enforcing data access controls, implementing authorization rules, and enforcing complex business logic that spans multiple tables or entities.

3. Batch Processing: Procedures are used for batch processing tasks that involve processing large volumes of data in scheduled or batch jobs. This can include tasks like data imports, data exports, data aggregation, and data cleanup operations.

4. Report Generation: Procedures are used to generate complex reports or aggregated data summaries. Procedures can retrieve data from multiple tables, perform calculations, apply filters, and generate formatted reports for users or external systems.

5. ETL (Extract, Transform, Load): Procedures are often used in ETL processes to extract data from various sources, transform it into a desired format, and load it into a target database or data warehouse. Procedures can handle data cleansing, data mapping, and data integration tasks.

6. Integration with External Systems: Procedures are used to integrate a database with external systems or APIs. They can perform data synchronization, trigger external actions based on database events, or retrieve data from external sources and update the database accordingly.

To retrieve the value returned by the procedure:

```SQL
-- 1. Output Parameters: If the procedure has output parameters defined, you can pass variables as parameters when calling the procedure, and the procedure will populate those variables with the returned values. Here's an example:

CREATE OR REPLACE PROCEDURE get_total_orders(
    OUT total INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT COUNT(*) INTO total FROM orders;
END;
$$;


DECLARE
    total_orders INTEGER;
BEGIN
    CALL get_total_orders(total_orders);
    -- The variable "total_orders" now contains the returned value
END;


-- 2. Returning a Single Value: If the procedure is designed to return a single value, you can use the RETURN statement within the procedure body to return the value. Then, when calling the procedure, you can capture the returned value using a variable or assign it directly to a column. Here's an example:

CREATE OR REPLACE PROCEDURE get_max_price()
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN MAX(price) FROM products;
END;
$$;


DECLARE
    max_price DECIMAL(10, 2);
BEGIN
    max_price := get_max_price();
    -- The variable "max_price" now contains the returned value
END;



-- 3. Returning Result Sets: If the procedure is designed to return a result set, you can use the RETURNS TABLE syntax to define the structure of the result set and return rows using the RETURN QUERY statement. When calling the procedure, you can capture the result set using a variable or use it directly in a query. Here's an example:

CREATE OR REPLACE PROCEDURE get_high_price_products()
RETURNS TABLE (
    id INTEGER,
    name VARCHAR(100),
    price DECIMAL(10, 2)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT id, name, price FROM products WHERE price > 100.00;
END;
$$;

-- To retrieve the result set:

DECLARE
    high_price_products TABLE (
        id INTEGER,
        name VARCHAR(100),
        price DECIMAL(10, 2)
    );
BEGIN
    high_price_products := get_high_price_products();
    -- The variable "high_price_products" now contains the result set
END;

```

We can also pass arguments into procedures 🤪

```SQL

CREATE OR REPLACE PROCEDURE calculate_area(length DECIMAL, width DECIMAL)
LANGUAGE plpgsql
AS $$
DECLARE
    area DECIMAL;
BEGIN
    -- Calculate the area using the provided length and width
    area := length * width;

    -- Do something with the calculated area
    -- ...

    -- Optionally, you can return the calculated area
    RETURN area;
END;
$$;


DECLARE
    rectangle_area DECIMAL;
BEGIN
    rectangle_area := calculate_area(5.0, 10.0);
    -- The variable "rectangle_area" now contains the calculated area
END;

```

💗 Benefits of using procedures 👍

1. Business Logic and Rules Enforcement:
   Stored procedures allow you to centralize and enforce business logic and rules within the database. This can include validating input data, applying complex calculations or transformations, enforcing data integrity constraints, and implementing business workflows. By encapsulating the logic in stored procedures, you ensure consistency and maintainability of the business rules across multiple applications and database interactions.
2. Performance Optimization:
   Stored procedures can help improve performance by reducing network traffic and optimizing execution plans. By encapsulating a series of SQL statements within a stored procedure, you minimize the back-and-forth communication between the application and the database, reducing network latency. Additionally, stored procedures can be compiled and cached, resulting in optimized execution plans, faster query execution, and reduced overhead.
3. Code Reusability and Maintenance:
   Stored procedures promote code reusability and maintainability. By encapsulating commonly used logic in stored procedures, you can avoid code duplication and ensure consistent implementation across different applications. This simplifies maintenance and updates, as changes can be made in a single location (the stored procedure) rather than modifying multiple instances of the same logic.
4. Transaction Control:
   Stored procedures enable you to manage transactions effectively. By grouping related operations within a stored procedure, you can control transaction boundaries and ensure atomicity, consistency, isolation, and durability (ACID) properties. This helps maintain data integrity and prevents data inconsistencies due to partial updates or failures.

### Indexing in Postgres and MongoDB

#### MongoDB and PostgreSQL are both popular database management systems (DBMS), but they differ in their approach to indexing. Here are the key differences between indexes in MongoDB and PostgreSQL:

1. Data Model:
   MongoDB is a document-based NoSQL database, where data is stored in flexible, schema-less documents in BSON (Binary JSON) format.
   PostgreSQL is a relational database, adhering to a structured data model with predefined schemas and tables.

2. Indexing Techniques:
   MongoDB primarily uses a B-tree index structure to index fields within documents. It supports single-field indexes, compound indexes (indexing multiple fields together), geospatial indexes, and text indexes for efficient text search.
   PostgreSQL uses various indexing techniques, including B-tree (default), hash, GiST (Generalized Search Tree), GIN (Generalized Inverted Index), and SP-GiST (Space-Partitioned Generalized Search Tree). These different index types allow PostgreSQL to optimize indexing for different data types and query patterns.

3. Indexing Flexibility:
   MongoDB provides more flexible indexing options since it operates on flexible schemas. You can create indexes on individual fields or combinations of fields within a document.
   PostgreSQL, being a relational database, requires predefined table schemas. Indexes are typically created on table columns and can span multiple columns to support complex queries involving joins and filtering.

4. Indexing Performance:
   MongoDB's indexing performance is optimized for high-speed read and write operations, especially when working with large amounts of unstructured or semi-structured data.
   PostgreSQL's indexing performance is generally well-suited for complex relational queries, joins, and aggregations. It offers various index types to handle specific data types and query patterns efficiently.

5. Index Maintenance:
   In MongoDB, indexes are automatically maintained as new documents are inserted, updated, or deleted. This can sometimes lead to increased storage requirements as the indexes grow.
   PostgreSQL requires manual maintenance of indexes, such as rebuilding or reindexing, to ensure optimal performance, especially after significant data changes.

6. Query Optimization:
   MongoDB's query optimizer considers the available indexes, query structure, and other factors to determine the most efficient execution plan for a query.
   PostgreSQL's query optimizer uses statistics and cost-based analysis to select the most efficient execution plan, considering indexes, join strategies, and other factors specific to relational queries.
   It's important to note that both MongoDB and PostgreSQL offer a range of features and configuration options related to indexing. The optimal choice depends on the specific requirements of your application and the type of data you're working with.

####

The choice between MongoDB and PostgreSQL for handling a large amount of data depends on various factors, including your specific use case, data structure, query patterns, scalability requirements, and the expertise of your development team. Here are a few considerations:

1. Data Structure and Flexibility:
   If your data has a flexible or evolving schema, MongoDB's document-based model may be advantageous. It allows you to store and query unstructured or semi-structured data more easily.
   If your data has a well-defined relational structure and requires complex joins and aggregations, PostgreSQL's relational model may provide a better fit.

2. Scalability:
   MongoDB is designed to scale horizontally, meaning it can distribute data across multiple servers or clusters to handle large datasets and high write loads efficiently. It offers built-in sharding capabilities for automatic data partitioning.
   PostgreSQL can also scale horizontally using techniques like table partitioning and replication, but it generally requires more manual configuration and effort compared to MongoDB.
3. Querying and Indexing:
   MongoDB's indexing capabilities are well-suited for high-speed read and write operations on unstructured or semi-structured data. It excels in scenarios where flexible queries and fast document retrieval are crucial.
   PostgreSQL's rich set of indexing techniques and optimization features make it a strong choice for complex relational queries, joins, and aggregations. It provides fine-grained control over indexing strategies and supports advanced query optimization techniques.

4. ACID Compliance and Transactions:
   PostgreSQL offers full ACID (Atomicity, Consistency, Isolation, Durability) compliance, making it suitable for applications that require strict data consistency and transactional integrity.
   MongoDB supports multi-document transactions starting from version 4.0, but it doesn't enforce ACID guarantees across multiple documents by default. It prioritizes high availability and scalability over strict consistency.

   What is ACID???

   - ACID compliance and transactions are typically needed in scenarios where data integrity, consistency, and reliability are critical. Here are some common use cases where ACID compliance and transactions are important:

ACID 1: Financial Systems:
Applications that handle financial transactions, banking systems, or payment processing require strict data consistency and transactional integrity. ACID compliance ensures that transactions are processed reliably, with proper isolation and atomicity.

ACID 2: E-commerce Platforms:
E-commerce systems often deal with complex operations involving inventory management, order processing, and payment transactions. ACID compliance guarantees that orders and inventory updates are consistent, and transactions are either committed in full or rolled back entirely.

ACID 3: Booking and Reservation Systems:
Systems that manage bookings, reservations, or event registrations rely on ACID compliance to ensure consistent updates and avoid conflicts or inconsistencies when multiple users attempt to reserve the same resource simultaneously.

ACID 4: Collaboration and Workflow Systems:
Applications that involve collaborative work, such as project management tools, document collaboration platforms, or task management systems, often require ACID compliance to maintain data consistency across multiple concurrent operations performed by different users.

ACID 5: Content Management Systems (CMS):
CMS applications that handle content creation, editing, and publication may benefit from ACID compliance to ensure proper versioning, content locking, and consistent updates across different components of the system.

ACID 6: Regulatory Compliance:
Industries such as healthcare, legal, or government sectors often have stringent regulatory requirements that demand data integrity and consistency. ACID compliance helps maintain accurate and auditable records, ensuring compliance with industry standards.

Examples with ACID in postgresql:

1. Basic Transaction:
   In this example, a new transaction is initiated with the BEGIN statement. The subsequent database operations are performed within the transaction, such as inserting a new user and updating an account balance. Finally, the COMMIT statement is used to commit the transaction, making the changes permanent.

```SQL

BEGIN; -- Start a new transaction

-- Perform your database operations within the transaction
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
UPDATE account SET balance = balance - 100 WHERE user_id = 123;

COMMIT; -- Commit the transaction

```

2. Rollback on Error:
   In this example, an error occurs while inserting an order item. The ROLLBACK statement is used to undo the entire transaction, including the previously inserted order, ensuring data consistency.

```SQL

BEGIN;

-- Perform database operations
INSERT INTO orders (order_id, customer_id, total_amount) VALUES (123, 456, 100.00);

-- Perform additional operations

-- Oops! An error occurred
INSERT INTO order_items (order_id, product_id, quantity) VALUES (123, 789, 2);

ROLLBACK; -- Rollback the transaction


```

3. Savepoints:
   In this example, a savepoint named sp1 is set within the transaction. The subsequent database operations occur, but an error occurs while inserting an order. The ROLLBACK TO SAVEPOINT statement is used to rollback the transaction to the savepoint, undoing the operations after the savepoint, and continuing with further operations.

```SQL
BEGIN;

-- Perform database operations
INSERT INTO customers (customer_id, name) VALUES (123, 'Alice');

SAVEPOINT sp1; -- Set a savepoint

-- More database operations
UPDATE account SET balance = balance + 500 WHERE customer_id = 123;

-- Oops! Another error occurred
INSERT INTO orders (order_id, customer_id) VALUES (789, 123);

ROLLBACK TO SAVEPOINT sp1; -- Rollback to the savepoint

-- Continue with more operations
UPDATE account SET balance = balance - 100 WHERE customer_id = 123;

COMMIT; -- Commit the transaction


```

5. Ecosystem and Community Support:
   PostgreSQL has been around for a long time and has a mature ecosystem with a large community of developers. It offers extensive tooling, libraries, and integration options.
   MongoDB has gained popularity in recent years and has a growing ecosystem. It provides its own set of tools, libraries, and integrations, particularly suitable for modern web and mobile applications.

### Normalization

Normalization is a technique of organizing the data into multiple related tables, to minimize `data redundancy`.

But first waht is data redundacy and why should we reduce it??

- Repetition of data in multiple places which increases the size of database.

1. 1st Normal Form
   ⚠️ 4 Rules:

   - Each column of you table must be single value
   - In each column each value stored must be the same type
   - Each column should have a unique name
   - Order in which data is saved doesn't matter

2. 2nd Normal Form
   ⚠️ 2 Rules:

   - It should complete the criteria of the 1NF
   - It should not have any `Partial Dependencies`

3. 3rd Normal Form

   - Should not have `Transital Dependencies`

## Work Training PostgreSQL -----------------------------

# Single Tenant VS Multi Tenant

# Define custom types

```SQL
CREATE TYPE compfoo AS (f1 int, f2, text);

CREATE TYPE bug_status AS ENUM()...
```

# JSON vs JSONB

GO into jsons in VS and do make clean. Do make seed. Do make populate-clean.
After that you can write code in query editor and do make query-editor.
After that do make columns-size which calculates the inserted data in size.

After it clean the data in tables and run make populate-dirty which inserts data which are not formated. After that when you compare the sizes you can see that jsonb has been optimised.
After that you can select \* from jsons.json_test you can see that data in jsonb has been optimised and formated.

In Advanded operations JSONB is a better choice and if you want to not change the formationg of your data go for JSON.

1. JSON
   Storage Format -> plain text format
   Indexing -> Supports it but is less efficient compared to JSONB.
   Query Performance -> Not as performant as JSONB
   Functionality -> Provides a basic set of functions for querying and manipulating JSON data.
2. JSONB
   Storage Format -> Stores Data in a binary format.
   Indexing -> Supports indexing using a more specialized and efficient indexing technique.
   Query performance -> Offerst better query performance since the binary format allows for more efficient storage and indexing.
   Functionality -> Offers a broader set of functions and operators for querying and maniputaling binary JSON data.

# Materialized Views

    Materialized views cannot be directly updated,
    fresh data can be generated for the materialized view with:

    ```SQL
    REFRESH MATERIALIZED VIEW mymatview;
    ```

Pros: fast reads and custom indexes
Cons: stale data until refresh, may block during refresh, takes space on disk ⚠️

You can also use incremental refreshing for materialized views:
https://www.alibabacloud.com/help/en/analyticdb-for-mysql/developer-reference/configure-incremental-refresh-for-materialized-views

# Inheritance Facts and Caveats

The child table inherits:

- NOT NULL constraints
- CHECK constraints

The child table does NOT inherit:

- PRIMARY KEY constraints
- UNIQUE constraints
- FOREIGN KEY constraints

Go to cd inheritances, and do make populate. Do make read-data. Here you can see all the inherited data.

You can use the keyword `ONLY` to see the data only from the rental table for example.

# Custom Operators and operations overloading.

# Window Functions

A window function performs a set of calculations across a set of table rows that are somehow related to the current row.

```SQL
SELECT depname, empno, salary, avg(salary) OVER (PARTITION  BY depname) FROM empsalary;
```

# Issues with Serial IDs

# Why UUIDs are a better solution

# Firebase pushID

# Vacuuming Tables (garbage collector for postgres)

# Partitioning

1- Range Partitioning
2- List Partitioning
3- Hash Partitioning

# Query Partitioning
