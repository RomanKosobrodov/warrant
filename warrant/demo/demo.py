import argparse
from warrant import Cognito


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sign in user to a Cognito User Pool")
    parser.add_argument("--user-pool", "-u",
                        help="User pool ID (including the region)",
                        type=str,
                        required=True)
    parser.add_argument("--client", "-c",
                        help="Client ID",
                        type=str,
                        required=True)
    parser.add_argument("--user-name", "-n",
                        help="User name",
                        type=str,
                        required=True)
    parser.add_argument("--password", "-p",
                        help="User password",
                        type=str,
                        required=True)
    args = parser.parse_args()

    u = Cognito(user_pool_id=args.user_pool,
                client_id=args.client,
                username=args.user_name)
    u.authenticate(password=args.password)

    print(f"Access token: \"{u.access_token}\"")
    print(f"Refresh token: \"{u.refresh_token}\"")
    print(f"ID token: \"{u.id_token}\"")
