FROM debian:stable-slim
COPY first_docker_server /bin/first_docker_server
ENV PORT=8991
CMD ["/bin/first_docker_server"]


