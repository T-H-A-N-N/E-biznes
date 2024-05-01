object DiscordBot {
    private const val discordWebhookUrl = "https://discord.com/api/webhooks/1235338831943827588/taOn9c7EPdzNM8Qo-0r1QFGDOWVd3LpVBS0ojAZDEkdcfVy8AnGqR27tHLLaj_eIH6aj"

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