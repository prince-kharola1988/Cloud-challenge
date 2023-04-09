# Creating Internet Gateway 
resource "aws_internet_gateway" "igwgateway" {
  vpc_id = "${aws_vpc.testvpc.id}"
}