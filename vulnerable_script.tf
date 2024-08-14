 resource "aws_launch_configuration" "bad_example" {
  associate_public_ip_address = true
    root_block_device {
        encrypted = false
    }
 }

resource "aws_cloudfront_distribution" "bad_example" {
  default_cache_behavior {
      viewer_protocol_policy = "allow-all"
    }
}
resource "aws_security_group" "bad_example" {
    egress {
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress{

    }
 }

 resource "aws_network_acl_rule" "bad_example" {
   egress         = false
   protocol       = "all"
   rule_action    = "allow"
   cidr_block     = "0.0.0.0/0"
 }


 resource "aws_neptune_cluster" "bad_example" {
   cluster_identifier                  = "neptune-cluster-demo"
   engine                              = "neptune"
   backup_retention_period             = 5
   preferred_backup_window             = "07:00-09:00"
   skip_final_snapshot                 = true
   iam_database_authentication_enabled = true
   apply_immediately                   = true
   storage_encrypted                   = false
 }

  resource "aws_db_instance" "bad_example" {
    publicly_accessible = true
 }


resource "aws_s3_bucket" "bad_example" {
    acl = "public-read"
}


 resource "kubernetes_network_policy" "bad_example" {
   metadata {
     name      = "terraform-example-network-policy"
     namespace = "default"
   }

   spec {
     pod_selector {
       match_expressions {
         key      = "name"
         operator = "In"
         values   = ["webfront", "api"]
       }
     }

     ingress {
       ports {
         port     = "http"
         protocol = "TCP"
       }
       ports {
         port     = "8125"
         protocol = "UDP"
       }

       from {
         ip_block {
           cidr = "0.0.0.0/0"
           except = [
             "10.0.0.0/24",
             "10.0.1.0/24",
           ]
         }
       }
     }

     egress {
       ports {
         port     = "http"
         protocol = "TCP"
       }
       ports {
         port     = "8125"
         protocol = "UDP"
       }

       to {
         ip_block {
           cidr = "0.0.0.0/0"
           except = [
             "10.0.0.0/24",
             "10.0.1.0/24",
           ]
         }
       }
     }

     policy_types = ["Ingress", "Egress"]
   }
 }

 resource "github_repository" "bad_example" {
   name        = "example"
   description = "My awesome codebase"

   visibility  = "public"

   template {
     owner = "github"
     repository = "terraform-module-template"
   }
 }

 
 resource "aws_instance" "bad_example" {
  ami = "ami-7f89a64f"
  instance_type = "t1.micro"

  root_block_device {
      encrypted = false
  }

  ebs_block_device {
    device_name = "/dev/sdg"
    volume_size = 5
    volume_type = "gp2"
    delete_on_termination = false
    encrypted = false
  }
}

resource "aws_kms_key" "bad_example" {
    enable_key_rotation = false
 }

 resource "aws_mq_broker" "bad_example" {
   broker_name = "example"

   configuration {
     id       = aws_mq_configuration.test.id
     revision = aws_mq_configuration.test.latest_revision
   }

   engine_type        = "ActiveMQ"
   engine_version     = "5.15.0"
   host_instance_type = "mq.t2.micro"
   security_groups    = [aws_security_group.test.id]

   user {
     username = "ExampleUser"
     password = "MindTheGap"
   }
   logs {
     audit = false
   }
   publicly_accessible = true
 }

 resource "aws_api_gateway_method_settings" "bad_example" {
    rest_api_id = aws_api_gateway_rest_api.example.id
    stage_name  = aws_api_gateway_stage.example.stage_name
    method_path = "path1/GET"
 
    settings {
      metrics_enabled = true
      logging_level   = "INFO"
      caching_enabled = true
      cache_data_encrypted = false
    }
  }

  resource "aws_api_gateway_stage" "bad_example" {
   stage_name    = "prod"
   rest_api_id   = aws_api_gateway_rest_api.test.id
   deployment_id = aws_api_gateway_deployment.test.id
   xray_tracing_enabled = false
 }

  resource "aws_iam_account_password_policy" "bad_example" {
    password_reuse_prevention = 1
 }