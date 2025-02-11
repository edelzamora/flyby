# Multi-stage build
# STAGE 1 - Build
FROM --platform=$BUILDPLATFORM golang:1.22 AS builder

# Container dir where bin will live
WORKDIR /app

# Copy Go module files and download dependencies
COPY go.mod go.sum ./
RUN go mod tidy

# Copy the source code
COPY . .

# Set up cross-compilation
ARG TARGETOS
ARG TARGETARCH
ENV GOOS=$TARGETOS GOARCH=$TARGETARCH CGO_ENABLED=0

# Build the application for the target architecture
RUN go build -o /flyby .

# STAGE 2 - Repackaged
# Final container
FROM --platform=$TARGETPLATFORM alpine:latest

# Environment Variable for microservice
ENV API_URL="http://"

# Container dir where bin will live
WORKDIR /app

# Copy compiled binary from builder stage
COPY --from=builder /flyby /app/flyby

# Copy HTML template files
COPY ./templates /app/templates

# Ensure the binary is executable
RUN chmod +x /app/flyby

# Expose application port
EXPOSE 3000

# Run the application
CMD ["/app/flyby"]
