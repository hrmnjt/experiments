# Simple example for producer and consumer


## Initial setup

Install confluent local - https://docs.confluent.io/platform/current/installation/installing_cp/zip-tar.html#

Setting up CLI - `CONFLUENT_HOME`
```bash
export CONFLUENT_HOME=${CONFLUENT_LOCATION}/confluent-6.0.0 \
    && echo "export CONFLUENT_HOME=$CONFLUENT_HOME" >> ~/.bashrc

# temporary setup for the session
# CONFLUENT_HOME=${CONFLUENT_LOCATION}/confluent-${CONFLUENT_VERSION}
```

Setting up CLI - Export to path
```bash
echo "export PATH=$CONFLUENT_HOME/bin:${PATH}" >> ~/.bashrc

# temporary setup for the session
# PATH=$CONFLUENT_HOME/bin:${PATH}"
```

Setting up CLI - bash completion (optional)
```bash
${CONFLUENT_LOCATION}/confluent-6.0.0/bin/confluent completion bash | sudo tee /etc/bash_completion.d/confluent \
    && echo "source /etc/bash_completion.d/confluent" >> ~/.bashrc \
    && source ~/.bashrc
```

Starting Services
```bash
confluent local services start
```

## Produce and Consume Avro Data

Create an Avro schema file
```bash
cat <<EOF > ~/temperature_reading.avsc
{
 "namespace": "io.confluent.examples",
 "type": "record",
 "name": "temperature_reading",
 "fields": [
    {"name": "city", "type": "string"},
    {"name": "temp", "type": "int", "doc": "temperature in Fahrenheit"} ]
}
EOF
```

Create a consume thread

```bash
confluent local services \
    kafka consume temperatures \
    --property print.key=true \
    --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
    --value-format avro
```

Create a produce thread

```bash
confluent local services \
    kafka produce temperatures \
    --property parse.key=true --property key.separator=, \
    --property key.serializer=org.apache.kafka.common.serialization.StringSerializer \
    --value-format avro \
    --property value.schema.file=$HOME/temperature_reading.avsc
```

Sample data on producer thread
```json
alameda,{"city":"alameda","temp":58}
ashland,{"city":"ashland","temp":62}
nairobi,{"city":"nairobi","temp":65}
sydney,{"city":"sydney","temp":75}
```

Sample bad data on producer thread
```json
jaipur,{"city":"jaipur","temp":"87"}
```
