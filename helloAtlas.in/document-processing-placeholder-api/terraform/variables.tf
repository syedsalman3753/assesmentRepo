variable "aws_region" {
  #default = ""
}

variable "app_name" {
  #default = ""
}

variable "container_port" {
  #default = 8000
  type = number
}

variable "alb_port" {
  #default = 80
  type = number
}

variable "image" {
  #default = ""
}
