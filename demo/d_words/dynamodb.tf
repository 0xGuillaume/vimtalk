resource "aws_dynamodb_table" "dynamodb" {
  name           = var.dynamodb.name
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = var.dynamodb.hash_key

  attribute {
    name = var.dynamodb.hash_key
    type = "S"
  }
}


resource "aws_dynamodb_table_item" "dynamodb" {
  for_each   = local.items
  #table_name = aws_dynamodb_table.dynamodb.name
  #hash_key   = aws_dynamodb_table.dynamodb.hash_key

  item = jsonencode(each.value)
}
