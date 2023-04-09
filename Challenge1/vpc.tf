# Creating VPC
resource "aws_vpc" "testvpc" {
  cidr_block       = "${var.vpc_cidr}"
  instance_tenancy = "default"

  tags = {
    Name = "Test VPC"
  }
}