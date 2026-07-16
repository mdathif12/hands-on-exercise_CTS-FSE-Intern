# Microservices Architecture

| Service Name | Responsibility | Endpoints | Database |
|-------------|---------------|------------|-----------|
| Course Service | Manage courses | /api/courses | course.db |
| Student Service | Manage students and enrollments | /api/students | student.db |
| Auth Service | Authentication and JWT validation | /api/auth | auth.db |
| Notification Service | Email notifications | /api/notifications | notification.db |

## Synchronous Communication (HTTP)

Advantages:
- Simple to implement
- Immediate response
- Easy debugging

Disadvantages:
- Tight coupling
- Service failures cascade
- Higher latency

## Asynchronous Communication (RabbitMQ/Kafka)

Advantages:
- Loosely coupled services
- Better scalability
- Fault tolerance

Disadvantages:
- Eventual consistency
- More infrastructure

## When to Use RabbitMQ or Kafka

Use message queues when:
- Sending emails
- Processing payments
- Audit logging
- High-volume event processing
- Long-running background tasks

Use HTTP when:
- Immediate response required
- Real-time validation needed
- Simple request-response workflows