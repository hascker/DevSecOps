#----------------------------------------------Stage 1 : Build Caddy----------------------------------------------------------------------------------------------
FROM golang:1.24-alpine AS builder

RUN apk add --no-cache git curl

WORKDIR /app

#Copy your forked Caddy repo into this image

COPY ./caddy /app

WORKDIR /app/cmd/caddy

RUN go build -o /caddy

#------------------------------------------Stage 2 : Minimal image---------------------------------------------------------------------------------------------------

FROM alpine:latest

RUN apk add --no-cache ca-certificates

COPY --from=builder /caddy /usr/bin/caddy

COPY Caddyfile /etc/caddy/Caddyfile

EXPOSE 80 443 

ENTRYPOINT ["caddy"]

CMD ["run","--config","/etc/caddy/Caddyfile","--adapter","caddyfile"]


