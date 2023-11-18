# Python Open Telementry in Plotly Dash

This example shows how one might collect metrics, traces, and logs in open telementry from a running dash application. Dash was chosen since I wanted to chose a framework out there that did not already have automatic instrumentation.

Additionally wanted to explore:
 - opentelementry-instrument and how far its "automagic" instrumentation would go in python
 - metrics through a collector -> prometheus
 - traces through a collector -> jaeger
 - still looking for a logging solution for experimentation (considered kafka)
