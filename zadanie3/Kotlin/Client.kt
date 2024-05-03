package client

import io.ktor.application.*
import io.ktor.response.*
import io.ktor.request.*
import io.ktor.routing.*
import io.ktor.http.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.features.json.*
import io.ktor.client.features.json.serializer.*
import io.ktor.client.request.*
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.Serializable
import io.ktor.client.request.*
import io.ktor.client.HttpClient


@Serializable
data class WebhookMessage(val content: String)
@Serializable
data class DiscordMessage(val content: String)
@Serializable
data class Product(val id: Int, val name: String, val price: Double)
@Serializable
data class SlackMessage(val text: String)


fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            post("/discord-webhook") {
                val message = call.receive<WebhookMessage>()
                if (message.content.startsWith("!products")) {
                    val category = message.content.removePrefix("!products").trim()
                    val products = getProductsByCategory(category)
                    val responseMessage = if (products.isNotEmpty()) {
                        "Products in $category: ${products.joinToString(", ") { it.name }}"
                    } else {
                        "No products found in category: $category"
                    }
                    Client.sendMessageToDiscord(responseMessage)
                }
                call.respond(HttpStatusCode.OK)
            }
        }
    }.start(wait = true)
}

object Client {
    private val httpClient = HttpClient(CIO) {
        install(JsonFeature) {
            serializer = KotlinxSerializer()
        }
    }

    private const val discordWebhookUrl = "https://discord.com/api/webhooks/1235338831943827588/taOn9c7EPdzNM8Qo-0r1QFGDOWVd3LpVBS0ojAZDEkdcfVy8AnGqR27tHLLaj_eIH6aj"
    private const val slackWebhookUrl = "https://hooks.slack.com/services/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"

    fun sendMessageToDiscord(message: String) {
        runBlocking {
            httpClient.post<Unit>(discordWebhookUrl) {
                contentType(ContentType.Application.Json)
                body = DiscordMessage(content = message)
            }
        }
    }
}

    fun sendMessageToSlack(message: String) {
        runBlocking {
            httpClient.post<Unit>(slackWebhookUrl) {
                contentType(ContentType.Application.Json)
                body = SlackMessage(text = message)
            }
        }
    }




@Serializable
data class Product(val id: Int, val name: String, val price: Double)

suspend fun getProductsByCategory(apiUrl: String, category: String): List<Product> {
    val httpClient = HttpClient(CIO) {
        install(JsonFeature) {
            serializer = KotlinxSerializer()
        }
    }
    return try {
        httpClient.get<List<Product>>("$apiUrl/products?category=$category")
    } catch (e: Exception) {
        println("Error fetching products: ${e.message}")
        emptyList()
    } finally {
        httpClient.close()
    }
}
