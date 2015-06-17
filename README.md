# Experimenting with ELK / JMeter PerfMon Server Agent

I have servers setup with the JMeter PerfMon Server Agent and would like to collect the [data provided](http://jmeter-plugins.org/wiki/PerfMonMetrics/) by this agent with Logstash to store it in Elasticsearch and visualise the data with Kibana.

The python script [logstash/perfmon.py](logstash/perfmon.py) is a telnet like client which is able to harvest data reported by the JMeter PerfMon Server Agent over the network.

With the Logstash [pipe](https://www.elastic.co/guide/en/logstash/master/plugins-inputs-pipe.html) input plugin we can collect those metrics easily.
