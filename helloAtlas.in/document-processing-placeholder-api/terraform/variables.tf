variable "aws_region" {
  default = "ap-south-1"
}

variable "app_name" {
  default = "document-processing-app"
}

variable "container_port" {
  default = 8000
}

variable "alb_port" {
  default = 80
}

variable "image" {
  default = "syedsalman041997/document-processing-placeholder-api:master"
}
