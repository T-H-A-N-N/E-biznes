package controllers

import javax.inject._
import play.api.mvc._
import play.api.libs.json._
import models.Category

@Singleton
class CategoryController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {
    var categories: List[Category] = List(
        Category(1, "Electronics"),
        Category(2, "Clothing")
    )

    def getAllCategories = Action {
        Ok(Json.toJson(categories))
    }

    def getCategory(id: Long) = Action {
        categories.find(_.id == id).map(category => Ok(Json.toJson(category))).getOrElse(NotFound)
    }

    def addCategory = Action(parse.json) { request =>
        request.body.validate[Category].map { category =>
            categories = categories :+ category
            Created(Json.toJson(category))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def updateCategory(id: Long) = Action(parse.json) { request =>
        request.body.validate[Category].map { category =>
            categories = categories.map {
                case c if c.id == id => category
                case c => c
            }
            Ok(Json.toJson(category))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def deleteCategory(id: Long) = Action {
        categories = categories.filterNot(_.id == id)
        NoContent
    }
}