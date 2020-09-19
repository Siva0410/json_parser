FROM ubuntu
LABEL maintainer="ichi"
RUN echo "Now building"
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Tokyo
RUN apt-get update && apt-get -y install apache2
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
