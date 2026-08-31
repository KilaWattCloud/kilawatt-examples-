"""
Kilawatt Cloud + CrewAI Integration Example
Demonstrates how to route autonomous agent compute requests through Kilawatt Cloud's zero-quota gateway.
"""

from kilawatt import Kilawatt

# Initialize Kilawatt Client in Sandbox Mode (Zero Cost)
client = Kilawatt(api_key="kw_test_sandbox_12345")

def execute_agent_cluster():
    print("Initializing CrewAI agent worker pool...")
    
    # Request 4x H100 GPU compute nodes for parallel agent execution
    deployment = client.deploy(
        gpu_type="nvidia-h100",
        count=4,
        dry_run=True  # Set dry_run=False when live API keys are active
    )
    
    print("Allocation Status:", deployment["status"])
    print("Failover Status:", deployment["reservation"]["region"])
    print("Egress Fee:", deployment["reservation"]["egress_fee"])

if __name__ == "__main__":
    execute_agent_cluster()
