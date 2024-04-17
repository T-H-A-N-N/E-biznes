package models

case class Cart(id: Long, items: List[CartItem]) {
  def totalCartPrice: Double = items.map(_.totalPrice).sum

  // Dodaj produkt do koszyka
  def addItem(newItem: CartItem): Cart = {
    items.find(_.productId == newItem.productId) match {
      case Some(existingItem) =>
        val updatedItems = items.map(item =>
          if (item.productId == newItem.productId) item.copy(quantity = item.quantity + newItem.quantity)
          else item
        )
        copy(items = updatedItems)
      case None =>
        copy(items = newItem :: items)
    }
  }

  // Usuń produkt z koszyka
  def removeItem(productId: Long): Cart = {
    copy(items = items.filterNot(_.productId == productId))
  }

  // Zaktualizuj ilość produktu w koszyku
  def updateItemQuantity(productId: Long, newQuantity: Int): Cart = {
    if (newQuantity > 0) {
      val updatedItems = items.map(item =>
        if (item.productId == productId) item.updateQuantity(newQuantity)
        else item
      )
      copy(items = updatedItems)
    } else {
      removeItem(productId)
    }
  }

  // Wyczyść koszyk
  def clearCart(): Cart = copy(items = List())
}