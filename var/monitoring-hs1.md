# Monitoring home server 1

Download page = https://prometheus.io/download/

## Setup `node_exporter`

Installing

```bash
cd ~/monitoring
wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz
tar xvzf node_exporter-1.1.2.linux-amd64.tar.gz
cd node_exporter-1.1.2.linux-amd64
```

Running

```bash
./node_exporter
```

UI: http://localhost:9100

## Setup `prometheus`

Installing

```bash
wget https://github.com/prometheus/prometheus/releases/download/v2.26.0/prometheus-2.26.0.linux-amd64.tar.gz
tar xvf prometheus-2.26.0.linux-amd64.tar.gz
cd prometheus-2.26.0.linux-amd64

mv prometheus.yml prometheus.yml.bk
```

Configuration - `prometheus.yml`

```yml
global:
  scrape_interval: 15s

scrape_configs:
- job_name: node
  static_configs:
  - targets: ['localhost:9100']
```

Running

```bash
./prometheus --config.file=./prometheus.yml
```

UI: http://localhost:9090
