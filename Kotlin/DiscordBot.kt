object DiscordBot {
    private const val discordWebhookUrl = "WEBHOOK_URL"

    fun sendMessage(message: String) {
        val client = HttpClient(CIO) {
            install(JsonFeature) {
                serializer = KotlinxSerializer()
            }
        }
        runBlocking {
            client.post<Unit>(discordWebhookUrl) {
                contentType(ContentType.Application.Json)
                body = DiscordMessage(content = message)
            }
        }
    }
}

@Serializable
data class DiscordMessage(val content: String)