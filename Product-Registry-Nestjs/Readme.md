Requests:

curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiVGVzdCBVc2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDk3MjI2NDIsImV4cCI6MTgxMjMxNDY0MiwidGVuYW50Ijp7ImlkIjoiNTUwZTg0MDAtZTI5Yi00MWQ0LWE3MTYtNDQ2NjU1NDQwMDAwIn0sImN1c3RvbURhdGEiOnsiYXR0cmlidXRlSWQiOiI5OTdlODUwMC1kNDViLTQxZTctYjk3NC01NTY2NTU0NDg4ODgifX0.J6y20NkgAhzc-SCstPR1E4xxhyJPObvblWU-J8mxOxU" http://localhost:3000/api/v1/product/7e201701-34a2-4b67-af78-6e821567ee0a/workspace/550e8400-e29b-41d4-a716-446655440000/997e8500-d45b-41e7-b974-556655448888

curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiVGVzdCBVc2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDk3MjI2NDIsImV4cCI6MTgxMjMxNDY0MiwidGVuYW50Ijp7ImlkIjoiNTUwZTg0MDAtZTI5Yi00MWQ0LWE3MTYtNDQ2NjU1NDQwMDAwIn0sImN1c3RvbURhdGEiOnsiYXR0cmlidXRlSWQiOiI5OTdlODUwMC1kNDViLTQxZTctYjk3NC01NTY2NTU0NDg4ODgifX0.J6y20NkgAhzc-SCstPR1E4xxhyJPObvblWU-J8mxOxU" http://localhost:3000/api/v1/product/workspace/550e8400-e29b-41d4-a716-446655440000/997e8500-d45b-41e7-b974-556655448888

curl -X POST 'http://localhost:3000/api/v1/product/create/workspace/550e8400-e29b-41d4-a716-446655440000/997e8500-d45b-41e7-b974-556655448888' -H 'Content-Type: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiVGVzdCBVc2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDk3MjI2NDIsImV4cCI6MTgxMjMxNDY0MiwidGVuYW50Ijp7ImlkIjoiNTUwZTg0MDAtZTI5Yi00MWQ0LWE3MTYtNDQ2NjU1NDQwMDAwIn0sImN1c3RvbURhdGEiOnsiYXR0cmlidXRlSWQiOiI5OTdlODUwMC1kNDViLTQxZTctYjk3NC01NTY2NTU0NDg4ODgifX0.J6y20NkgAhzc-SCstPR1E4xxhyJPObvblWU-J8mxOxU' -d '{
"name": "Test Product",
"description": "This is a test product",
"product_code": "TP002",
"workspace_id": "550e8400-e29b-41d4-a716-446655440000",
"workspace_attribute_id": "997e8500-d45b-41e7-b974-556655448888"
}'

curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiVGVzdCBVc2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDk3MjI2NDIsImV4cCI6MTgxMjMxNDY0MiwidGVuYW50Ijp7ImlkIjoiNTUwZTg0MDAtZTI5Yi00MWQ0LWE3MTYtNDQ2NjU1NDQwMDAwIn0sImN1c3RvbURhdGEiOnsiYXR0cmlidXRlSWQiOiI5OTdlODUwMC1kNDViLTQxZTctYjk3NC01NTY2NTU0NDg4ODgifX0.J6y20NkgAhzc-SCstPR1E4xxhyJPObvblWU-J8mxOxU" http://localhost:3000/api/v1/product/7e201701-34a2-4b67-af78-6e821567ee0a/workspace//997e8500-d45b-41e7-b974-556655448888

curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiVGVzdCBVc2VyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDk3MjI2NDIsImV4cCI6MTgxMjMxNDY0MiwidGVuYW50Ijp7ImlkIjoiNTUwZTg0MDAtZTI5Yi00MWQ0LWE3MTYtNDQ2NjU1NDQwMDAwIn0sImN1c3RvbURhdGEiOnsiYXR0cmlidXRlSWQiOiI5OTdlODUwMC1kNDViLTQxZTctYjk3NC01NTY2NTU0NDg4ODgifX0.J6y20NkgAhzc-SCstPR1E4xxhyJPObvblWU-J8mxOxU" http://localhost:3000/api/v1/product?workspace_id=550e8400-e29b-41d4-a716-446655440000&workspace_attribute_id=997e8500-d45b-41e7-b974-556655448888

# NestJS Request Parameters: A Complete Guide

NestJS offers a rich set of decorators to extract data from different parts of an HTTP request. Beyond the basic path and query parameters, there are several other parameter types and advanced techniques for working with them.

1. Path Parameters (@Param)

```typescript
@Get('users/:id')
getUser(@Param('id') id: string) {
  return `User ID: ${id}`;
}
```

2. Query Params (@Query)

```typescript
@Get('search')
search(@Query('term') searchTerm: string) {
  return `Searching for: ${searchTerm}`;
}
```

3. Request Body (@Body)

```typescript
@Post()
create(@Body() createUserDto: CreateUserDto) {
  return `Creating user: ${createUserDto.name}`;
}
```

4. Headers (@Headers)

```typescript
@Get()
findAll(@Headers() headers: Record<string, string>) {
  console.log(headers['user-agent']);
  return 'This action returns all items';
}
```

5. Request Object (@Req or @Request)

```typescript
@Get()
findAll(@Req() request: Request) {
  const url = request.url;
  const method = request.method;
  return 'This action returns all items';
}
```

6. Response Object (@Res or @Response)

```typescript
@Get()
findAll(@Res() response: Response) {
  return response.status(200).json({
    message: 'This action returns all items'
  });
}
```

7. Cookie Params (@Cookies)

```typescript
@Get()
findAll(@Cookies('auth') authCookie: string) {
  return `Auth cookie: ${authCookie}`;
}
```

8. Session Data (@Session)

Access session data (requires express-session middleware):

```typescript
@Get()
findAll(@Session() session: Record<string, any>) {
  session.visits = session.visits ? session.visits + 1 : 1;
  return `Visited ${session.visits} times`;
}
```

9. File Upload (@UploadedFile and @UploadedFiles)

```typescript
@Post('upload')
@UseInterceptors(FileInterceptor('file'))
uploadFile(@UploadedFile() file: Express.Multer.File) {
  return {
    filename: file.filename,
    size: file.size
  };
}
```

- Examples and Technicues

1. Custom Pipes for Transformation Validation
   Pipes can transform input data and validate it before it reaches your route handlers:

```typescript
@Post('upload')
// A custom pipe to parse comma-separated values
@Injectable()
export class ParseArrayPipe implements PipeTransform {
  transform(value: string): string[] {
    if (!value) return [];
    return value.split(',').map(item => item.trim());
  }
}

@Get()
findByTags(@Query('tags', ParseArrayPipe) tags: string[]) {
  return `Searching for tags: ${tags.join(', ')}`;
}
```

## Company Registry

Tenancy information workspace-id + workspace-attribute-id
Tenancy in fic for fic is not fully done

Fic-Api-V2 will act as a proxy...

# Prisma

- npx prisma migrate dev --name rename_product_to_trade_item --create-only
- npx prisma migrate dev --name rename_product_to_trade_item

## Dapr and Redis

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration -H "Content-Type: application/json" -d '{"products":[{"id":"123","name":"Test6666666666666666666666666t", "workspace_id": "123e4567-e89b-12d3-a456-426614174000
}]}'

👍
curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=" \
 -d '{"products":[{"id":"123","name":"Test6666666666666666666666666t", "workspace_id": "db2d9052-dfa0-44ed-8991-5f9919735ab3"}]}'

👍
curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration\trade-items \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=" \
 -d '{
"type": "create",
"products": [{
"name": "Test Item via Curl",
"description": "This is a test item created via curl",
"code": "TEST-001",
"workspace_id": "workspace-123"
}]
}'

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items -H "Content-Type: application/json" -H "dapr-app-id: trade-items-write" -H "dapr-api-token: CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=" -d '{
"type": "create",
"items": [{
"name": "Test Item via Curl",
"description": "This is a test item created via curl",
"code": "TEST-001",
"workspace_id": "workspace-123"
}]
}'

⚠️
curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=" \
 -d '{"products":[{"id":"123","name":"Test6666666666666666666666666t", "workspace_id": "db2d9052-dfa0-44ed-8991-5f9919735ab3"}]}'

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration -H "Content-Type: application/json" -d '{"products":[{"id":"123","name":"Test6666666666666666666666666t", "workspace_id": "60d8d4ab-fe71-4872-b5b9-d3e9219e8a5a"}]}'

Doesnt work, find out why: curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration -H "Content-Type: application/json" -d '{"products":[{"id":"123","name":"Test Produc 2t", "workspace_id": "123e4567-e89b-12d3-a456-426614174000"}]}'

docker exec -it redis redis-cli -p 6371 PUBLISH product-migration '{"id":"123","action":"create"}'

These are the core things:

1. A `DaprService` class that handles communication with the Dapr runtime
2. A `RedisService` class that manages direct Redis connections
3. An `EventsController` and Dapr component configuration files

Together, these create a system where your NestJS application can publish and subscribe to events through Dapr, with Redis as the underlying message broker.

`EventsController`:

```javascript
@Controller('events')
export class EventsController {
  private readonly logger = new Logger(EventsController.name);


// This is the endpoint that actually receives the event data when something is published to the "product-migration" topic.
// The function logs the incoming data and returns a success response. In a complete implementation, you would process the event data here.
// You can create as much endpoints as you want to handle the events comming from dapr
// This is called from the dapr service
  @Post('product-migration')
  handleProductMigration(@Body() data: any) {
    this.logger.log(
      `Received product migration event: ${JSON.stringify(data)}`,
    );
    // Process the event in future
    return { success: true };
  }
}
```

`DaprService`:

```javascript

import { Injectable, OnModuleInit, Logger, Optional } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { DaprClient, DaprServer } from '@dapr/dapr';

@Injectable()
export class DaprService implements OnModuleInit {
  private daprClient: DaprClient | null = null;
  private daprServer: DaprServer | null = null;
  private readonly logger = new Logger(DaprService.name);
  private serverInitialized = false;
  private isDaprAvailable = false;

  constructor(private configService: ConfigService) {}

  async onModuleInit() {
    try {
      // Add a small delay to give Dapr sidecar time to initialize
      this.logger.log('Waiting for Dapr sidecar to initialize...');
      await new Promise((resolve) => setTimeout(resolve, 2000));

      const daprHost =
        this.configService.get<string>('DAPR_HOST') || 'localhost';
      const daprHttpPort =
        this.configService.get<string>('DAPR_HTTP_PORT') || '3500';
      const daprGrpcPort =
        this.configService.get<string>('DAPR_GRPC_PORT') || '50001';

      this.logger.log(`Connecting to Dapr at ${daprHost}:${daprHttpPort}...`);

      let retries = 0;
      const maxRetries = 5;

      while (retries < maxRetries) {
        try {
          this.daprClient = new DaprClient({
            daprHost,
            daprPort: daprHttpPort,
          });

          await this.daprClient.metadata.get();
          this.isDaprAvailable = true;
          this.logger.log('Successfully connected to Dapr sidecar');
          break;
        } catch (error) {
          retries++;
          this.logger.warn(
            `Failed to connect to Dapr, attempt ${retries}/${maxRetries}: ${error.message}`,
          );

          if (retries >= maxRetries) {
            this.logger.error('All Dapr connection attempts failed');
            this.isDaprAvailable = false;
            return;
          }

          // Exponential backoff
          const delay = Math.min(Math.pow(2, retries) * 500, 5000);
          await new Promise((resolve) => setTimeout(resolve, delay));
        }
      }

      // Rest of your initialization logic...
    } catch (error) {
      this.logger.error(
        `Dapr initialization error: ${error.message}`,
        error.stack,
      );
      this.isDaprAvailable = false;
    }
  }

  isDaprEnabled(): boolean {
    return this.isDaprAvailable;
  }

  getClient(): DaprClient | null {
    return this.daprClient;
  }

  getServer(): DaprServer | null {
    return this.daprServer;
  }

  async publishEvent(
    pubsubName: string,
    topicName: string,
    data: any,
  ): Promise<boolean> {
    if (!this.isDaprAvailable || !this.daprClient) {
      this.logger.warn(
        `Cannot publish event: Dapr is not available. Event to ${pubsubName}/${topicName} discarded.`,
      );
      return false;
    }

    try {
      this.logger.log(`Publishing event to ${pubsubName}/${topicName}`);
      await this.daprClient.pubsub.publish(pubsubName, topicName, data);
      this.logger.log('Event published successfully');
      return true;
    } catch (error) {
      this.logger.error(
        `Failed to publish event: ${error.message}`,
        error.stack,
      );
      return false;
    }
  }

// subscribeToTopic(): Programmatically subscribes to topics (an alternative to the controller-based approach) This is called in the prisma-trade-items-repository in setupDaprSubscription on initialization
  async subscribeToTopic(
    pubsubName: string,
    topicName: string,
    callback: (data: any) => Promise<void>,
  ): Promise<boolean> {
    if (!this.isDaprAvailable) {
      this.logger.warn(
        `Cannot subscribe to topic: Dapr is not available. Subscription to ${pubsubName}/${topicName} skipped.`,
      );
      return false;
    }

    try {
      // Wait for server to be initialized if needed (with timeout)
      if (!this.serverInitialized) {
        this.logger.warn(
          `Dapr server not yet initialized. Waiting before subscribing to ${topicName}...`,
        );
        let isInitialized = await this.waitForInitialization(5000); // 5 second timeout

        if (!isInitialized) {
          this.logger.warn(
            `Timed out waiting for Dapr server initialization. Subscription to ${topicName} skipped.`,
          );
          return false;
        }
      }

      if (!this.daprServer) {
        this.logger.warn(
          `Cannot subscribe: Dapr server is not initialized. Subscription to ${topicName} skipped.`,
        );
        return false;
      }

      this.logger.log(`Subscribing to topic ${pubsubName}/${topicName}`);
      this.daprServer.pubsub.subscribe(pubsubName, topicName, callback);
      this.logger.log(`Successfully subscribed to ${pubsubName}/${topicName}`);
      return true;
    } catch (error) {
      this.logger.error(
        `Failed to subscribe to topic: ${error.message}`,
        error.stack,
      );
      return false;
    }
  }

  async startServer(): Promise<boolean> {
    if (!this.isDaprAvailable) {
      this.logger.warn('Cannot start server: Dapr is not available');
      return false;
    }

    try {
      if (!this.daprServer) {
        this.logger.warn('Cannot start server: Dapr server is not initialized');
        return false;
      }

      if (!this.serverInitialized) {
        this.logger.log('Starting Dapr server...');
        await this.daprServer.start();
        this.serverInitialized = true;
        this.logger.log('Dapr server started successfully');
        return true;
      } else {
        this.logger.log('Dapr server already started');
        return true;
      }
    } catch (error) {
      this.logger.error(
        `Failed to start Dapr server: ${error.message}`,
        error.stack,
      );
      return false;
    }
  }

  private async waitForInitialization(timeoutMs: number): Promise<boolean> {
    return new Promise<boolean>((resolve) => {
      const startTime = Date.now();
      const checkInterval = setInterval(() => {
        if (this.serverInitialized) {
          clearInterval(checkInterval);
          resolve(true);
        } else if (Date.now() - startTime > timeoutMs) {
          clearInterval(checkInterval);
          resolve(false);
        }
      }, 100);
    });
  }
}
```

sudo chown -R $(whoami) /home/admir/work-projects/product_registry/dist/

-- When git token expires
Personal access token:: 9ciUCFjdcvNXK5dGgHLf

git remote set-url origin https://a.demaj:9ciUCFjdcvNXK5dGgHLf@biosphere.teamsystem.com/oneplatform/islands/microsme/product_registry

export DATABASE_URL=$(./get-db-url.sh)
npx prisma migrate deploy
npx prisma generate
npx nest build read
npm run start:read:debug

- ~/.azure:/root/.azure

root@913754b3fca3:/var/www/product-registry# psql -h $PGHOST -U $PGUSER -d $PGDATABASE -p $PGPORT
psql: error: connection to server at "product-registry-dev-westeurope-pgsql-flex.postgres.database.azure.com" (13.95.228.156), port 5432 failed: FATAL: password authentication failed for user "a.demaj@product-registry-dev"

docker exec -it product-registry-read bash

apt-get update && apt-get install -y postgresql-client

psql

# First, get the token and verify it looks reasonable

TOKEN=$(az account get-access-token --resource https://ossrdbms-aad.database.windows.net --query accessToken --output tsv)
echo "Token length: ${#TOKEN}"

# Export as PGPASSWORD

export PGPASSWORD="$TOKEN"

# Try connecting with simplest settings

export PGHOST=product-registry-dev-westeurope-pgsql-flex.postgres.database.azure.com
export PGUSER="email@product-registry-dev"
export PGPORT=5432
export PGDATABASE=postgres
export PGSSLMODE=require

# Connect with explicit parameters

psql -h $PGHOST -U $PGUSER -d $PGDATABASE -p $PGPORT

## M2M

# Generate a random 32-byte token and encode it as base64

TOKEN=$(openssl rand -base64 32)
echo "Generated API Token: $TOKEN"

# Save this token securely - you'll need it in multiple places

Generated API Token: ti2kk+DRrWabxWeo1fN6hnKjN599XASWmIq/iDkFkmQ=
CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=

For kubernetes: echo -n "CZHIwa0Tzh8yPR4yb081YebDI8cOTEVajjwvglwWQts=" | base64 -> Q1pISXdhMFR6aDh5UFI0eWIwODFZZWJESThjT1RFVmFqand2Z2x3V1F0cz0=

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: ti2kk+DRrWabxWeo1fN6hnKjN599XASWmIq/iDkFkmQ=" \
 -d '{"products":[{"id":"123","name":"Test Product"}]}'

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: ti2kk+DRrWabxWeo1fN6hnKjN599XASWmIq/iDkFkmQ=" \
 -d '{
"products": [{"id":"123","name":"Test Product"}],
"authentication": {
"token": "test"
}
}'

curl -X POST http://localhost:3501/v1.0/publish/pubsub/trade-items-migration \
 -H "Content-Type: application/json" \
 -H "dapr-api-token: ti2kk+DRrWabxWeo1fN6hnKjN599XASWmIq/iDkFkmQ=" \
 -d '{
"products": [{"id":"123","name":"Test Product"}],
"authentication": {
"token": "bXlTdHJvbmdTZWNyZXRLZXkxMjM0NTY3ODlUZXN0VGVzdA=="
}
}'

#!/bin/bash

# Run database migrations and generate client

echo "Running Prisma migrations and generating client..."
npx prisma migrate deploy
npx prisma generate

# Run the initial build

echo "Building the write module..."
npm run build:write

# Start TypeScript compiler in watch mode in the background

echo "Starting TypeScript compiler in watch mode..."
npx tsc -p tsconfig.write.json --watch &
TS_COMPILER_PID=$!

# Set up a trap to kill the TypeScript compiler when this script exits

trap "kill $TS_COMPILER_PID" EXIT

# Set environment variables

export SERVICE_NAME=write
export PORT=3011
export DAPR_HTTP_PORT=3501
export DAPR_GRPC_PORT=50002

# Start nodemon directly without concurrently

echo "Starting nodemon to watch for changes..."
npx nodemon --watch dist/write dist/write/write/main.js

# ⚠️ Learnnn thisss:

prisma.$use()
