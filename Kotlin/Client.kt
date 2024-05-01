package client

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.features.json.*
import io.ktor.client.features.json.serializer.*
import io.ktor.client.request.*
import io.ktor.http.*
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.Serializable

object Client {
    private val httpClient = HttpClient(CIO) {
        install(JsonFeature) {
            serializer = KotlinxSerializer()
        }
    }

    private const val discordWebhookUrl = "https://discord.com/api/webhooks/1235338831943827588/taOn9c7EPdzNM8Qo-0r1QFGDOWVd3LpVBS0ojAZDEkdcfVy8AnGqR27tHLLaj_eIH6aj"

    fun sendMessageToDiscord(message: String) {
        runBlocking {
            httpClient.post<Unit>(discordWebhookUrl) {
                contentType(ContentType.Application.Json)
                body = DiscordMessage(content = message)
            }
        }
    }
}

@Serializable
data class DiscordMessage(val content: String)