package models

import play.api.data._
import play.api.data.Forms._

case class Category(id: Long, name: String, description: Option[String])

object Category {
  val categoryForm: Form[Category] = Form(
    mapping(
      "id" -> longNumber,
      "name" -> nonEmptyText,
      "description" -> optional(text)
    )(Category.apply)(Category.unapply)
  )
}