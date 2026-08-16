from client import EnterpriseAgentPermissionBoundaryGovernorClient

def main():
    client = EnterpriseAgentPermissionBoundaryGovernorClient()
    res = client.authorize_action("agent_support_01", "READ_CUSTOMER_TICKET", "db://tickets/tenant_42")
    print(f"Access Granted: {res['access_granted']}")
    print(f"Policy Decision: {res['policy_decision']}")
    print(f"Audit Log ID: {res['audit_log_id']}")

if __name__ == "__main__":
    main()
