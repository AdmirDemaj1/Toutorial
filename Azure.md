https://esi.learnondemand.net/
Account for azure microsoft.
ademajj12@outlook.com
ademaj1222@@AD

# Creating Azure App Service Web Apps -- Monolithic

--> html based web apps (HTTP(S))
--> API/Backends FOR WEB/MOBILE (gRPC)

-- Scalability and Performance
Authentication and Authorization
Monitoring and Analytics
DevOps and CI/CD
Security Services
Networking:

1. Azure Virtual Network: Isolate and secure your application's network traffic.
2. Azure Application Gateway: Optimize and secure the delivery of your web applications.

## 3 types of plans:

Shared Dedicated Isolated

Scale out (you want it to be done automatically)
Sclae up (you dont want to do it automatically)

Steps: We created a plan in portal.azure.com and inside that plan we cretaed two applications one in .net and one on node.js 18, remember we are paying for the plan. We can stop one of the applications but still we would pay.

After that we edited the configuration of our app including auth, colour, site, and dbconn.
We also for each application can add a new security provider like apple, microsoft, facebook etc.

After that we added a custom domain "news.com....".
Later we had a look at networking -> inbound traffic -> access restrictions to put a range for ip addresses.
Later we changed the diagnostic settings

## Adding a new Deployment slot

Deployment slots in Microsoft Azure provide a way to host different versions of your application in the same Azure App Service. These slots allow you to deploy and test new versions of your application without affecting the production environment.

⚠️ Take note::: there is no way to specify the scalability for eact deployment slot in Azure App Service so we dont have fully control for it but we can control it by instances we can run the slots in specific instances.

## Dynamic App Code and Static Content

- Dynamic
  .net .node

- Static web App
  .html .js (logic connects in the browser)

---===---===---===---===---===

# Implement Azure function Apps -- Microservices

--> execute some code (schedule, http(s), azure service)
--> microServices

---===---===---===---===---===

# Storage Account

Types of storages:

- blob/containers
- files
- queues
- tables
  ⚠️ Keep in mind that storage is not _compute_ like azure function apps and app services!
  --> Storage durability options: LRS ZRS GRS RA-GRS

# Cosmos DB Storage

Azure Cosmos DB has logical partitioning which allows for horizontal scailing by distributing data across logical partitions. Each partition can be independently scaled, allowing the system to handle a massive volume of data and on high throughput.

Get out the idea of "tables" when you talk about cosmos DB. (Dont think about tables.)

It offers a variety of API:
MongoDB API
Table API
Gremlin API
Cassandra API
SQL API
.....

# Implement container solutions

# Auth and Auth

- MSAL -----------
  -------> registered apps
- graphAPI ---------

# Impelemt secure cloud solutions

# Event-driven architecture

## Event Grid, event Hub and service hub

### Queues vs Topics, in queues there is only one reciever/consumer and in topics there are many consumers.

- Event grid might be user registration or when the rifridgerated truck stops sending information back.
- event hub is a collection of requests that in the end manage a functionality (example with rifridgerated truck sensor sending information every time).

Implement API Management
Develop event-based solutions
Develop message-based solutions
Instrument solution to support monitoring and logging
Integrate caching and content delivery within solutions

# Azure Cache for Redis

Limited Query Functionality: Redis has limited query functionality2. By design, it only provides primary key access2. Query functionality can be extended with third-party Redis Modules2, but this requires additional setup and maintenance.

When You’ll Have More Data Than You Have Memory: Redis is in-memory. If there’s a chance that your data will grow past the size of your server’s RAM, Redis is the wrong choice1.

When You Need to Preserve Data Types: If you need to keep your numbers as numeric types, your dates as Date types, or keep a hold on other non-string primitives, Redis isn’t the answer1.
