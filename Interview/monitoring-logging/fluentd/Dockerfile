# fluentd/Dockerfile

FROM fluent/fluentd:edge-debian

USER root

# Install Loki output plugin
RUN gem install fluent-plugin-grafana-loki --no-document

# (Optional) Install S3 output plugin
RUN gem install fluent-plugin-s3 --no-document

# Install Docker metadata plugin
RUN gem install fluent-plugin-docker_metadata_filter --no-document

# Clean up to keep image small
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER fluent
