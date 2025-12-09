# Monitoring Alerts

This document outlines the alerting strategy for the AI Prime service.

## High Priority Alerts (P1)

- **API Availability Below SLO**: Fires when the API availability drops below 99.9% over a 5-minute period.
- **API Latency Exceeds SLO**: Fires when the 99th percentile of API query latency exceeds 2000ms over a 5-minute period.
- **High 5xx Error Rate**: Fires when the rate of 5xx errors exceeds 1% of total requests over a 5-minute period.

## Low Priority Alerts (P2)

- **High 4xx Error Rate**: Fires when the rate of 4xx errors exceeds 5% of total requests over a 15-minute period.
- **High CPU/Memory Usage**: Fires when CPU or memory usage of a service exceeds 80% for a sustained period.
- **Redis Cache Saturation**: Fires when Redis memory usage is above 90%.
