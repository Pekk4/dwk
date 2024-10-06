FROM golang:1.21.1-alpine3.18 AS build-stage

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /app/server


FROM scratch

WORKDIR /app

EXPOSE 8080

COPY --from=build-stage /app/server /app/server

CMD ["./server"]