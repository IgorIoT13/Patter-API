import json
from config import OUTPUT_STRATEGY, KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, REDIS_HOST, REDIS_PORT, REDIS_LIST

class OutputStrategy:
    def output(self, data):
        raise NotImplementedError

class ConsoleOutputStrategy(OutputStrategy):
    def output(self, data):
        for row in data:
            print(row)

class KafkaOutputStrategy(OutputStrategy):
    def __init__(self):
        from kafka import KafkaProducer
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    def output(self, data):
        for row in data:
            self.producer.send(KAFKA_TOPIC, row)
        self.producer.flush()

class RedisOutputStrategy(OutputStrategy):
    def __init__(self):
        import redis
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    def output(self, data):
        for row in data:
            self.r.rpush(REDIS_LIST, json.dumps(row))

def get_strategy():
    if OUTPUT_STRATEGY == "console":
        return ConsoleOutputStrategy()
    elif OUTPUT_STRATEGY == "kafka":
        return KafkaOutputStrategy()
    elif OUTPUT_STRATEGY == "redis":
        return RedisOutputStrategy()
    else:
        raise ValueError(f"Unknown strategy: {OUTPUT_STRATEGY}")
