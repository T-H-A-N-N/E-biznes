import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.routing.*
import io.ktor.application.*
import io.ktor.response.*
import io.ktor.request.*
import client.Client

fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/") {
                call.respondText("Hello, world!")
            }
            post("/message") {
                val message = call.receive<String>()
                Client.sendMessageToDiscord(message)
                call.respondText("Message sent to Discord")
            }
        }
    }.start(wait = true)
}