package models

case class CartItem(productId: Long, quantity: Int, pricePerItem: Double) {
  def totalPrice: Double = quantity * pricePerItem

  // Metoda do aktualizacji ilości produktów w pozycji koszyka
  def updateQuantity(newQuantity: Int): CartItem = {
    copy(quantity = newQuantity)
  }
}