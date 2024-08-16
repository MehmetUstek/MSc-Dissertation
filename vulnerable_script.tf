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

 resource "aws_security_group" "bad_example" {
   name        = "http"

   ingress {
     description = "HTTP from VPC"
     from_port   = 80
     to_port     = 80
     protocol    = "tcp"
     cidr_blocks = [aws_vpc.main.cidr_block]
   }
 }

  resource "aws_ecs_cluster" "bad_example" {
    name = "services-cluster"
 }

 resource "aws_docdb_cluster" "bad_example" {
   cluster_identifier      = "my-docdb-cluster"
   engine                  = "docdb"
   master_username         = "foo"
   master_password         = "mustbeeightchars"
   backup_retention_period = 5
   preferred_backup_window = "07:00-09:00"
   skip_final_snapshot     = true
   storage_encrypted = false
   enabled_cloudwatch_logs_exports = "something"
 }

 resource "github_branch_protection" "bad_example" {
   repository_id = "example"
   pattern       = "main"

   require_signed_commits = false
 }
