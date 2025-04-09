import pyroscope

pyroscope.configure(
    application_name = "app.app",
    server_address = "http://127.0.0.1:4040"
)