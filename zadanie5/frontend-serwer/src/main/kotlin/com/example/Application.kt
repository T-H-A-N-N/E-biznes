package com.example

import io.ktor.application.*
import io.ktor.features.*
import io.ktor.gson.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

data class Produkt(val id: Int, val nazwa: String, val cena: Double)

fun main() {
    val produkty = listOf(
        Produkt(1, "Produkt 1", 10.0),
        Produkt(2, "Produkt 2", 40.0),
        Produkt(3, "Produkt 3", 90.0)
    )

    val server = embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            gson {
                setPrettyPrinting()
            }
        }

        routing {
            route("/api") {
                get("/produkty") {
                    call.respond(produkty)
                }

                post("/platnosci") {
                    val data = call.receive<Map<String, Any>>()
                    val kwota = data["kwota"] as Double
                    // Płatność(nie wymagany kod?)
                    call.respond(mapOf("success" to true, "kwota" to kwota))
                }
            }
        }
    }
    server.start(wait = true)
}