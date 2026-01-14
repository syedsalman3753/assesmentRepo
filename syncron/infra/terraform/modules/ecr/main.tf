terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.28.0"
    }
    aap = {
      source  = "ansible/aap"
      version = "1.3.0"
    }
  }
}

variable "AWS_REGION" {
  type = string
  default = "ap-south-1a"
}
# DOCKER IMAGE WITH TAG
variable "DOCKER_IMAGE_TAG" {
  type = string
  default = "nginx:latest"
}

provider "aws" {
  region = var.AWS_REGION
}

resource "null_resource" "dockerpull" {
  triggers = {hash(existone, new)}
  provisioner "local-exec" {
    inline = [
      echo password | docker login -u username

      docker tag ecr

      docker push var.DOCKER_IMAGE_TAG
    ]
  }
}

variable "sq" {
  type = set(map(list))

}

locals {

  sg = [
    appp = [
       ing_rule = {}
       eg_rule = {}
    ]

  ]


}
resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4" {
  for_each = local.sg

  dynamic "" {
    for_each = ""
    content {
      security_group_id = aws_security_group.allow_tls.id
      cidr_ipv4         = aws_vpc.main.cidr_block
      from_port         = 443
      ip_protocol       = "tcp"
      to_port           = 443

    }
  }

}