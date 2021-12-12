#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;

#define pb push_back
#define all(x) begin(x), end(x)
#define sz(x) (int) (x).size()

using pi = pair<int,int>;

#define f first
#define s second
#define mp make_pair

// literally impossible to do recursive dfs in python

vi dx = {1, 0, -1, 0};
vi dy = {0, 1, 0, -1};

bool vis[105][105];
vector<vi> vals(101, vi(101));
set<pi> cur;

void dfs(int x, int y) {
	vis[x][y] = true;
	cur.insert({x, y});

	for (int k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];

		if (nx < 0 || nx >= 100 || ny < 0 || ny >= 100) {
			continue;
		}
		
		if (!vis[nx][ny] && vals[nx][ny] != 9) {
			dfs(nx, ny);
		}
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	vector<pi> lows;

	for (int i = 0; i < 100; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 100; j++) {
			vals[i][j] = s.at(j) - '0';
		}
	}

	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			bool islow = true;

			for (int k = 0; k < 4; k++) {
				int x = i + dx[k];
				int y = j + dy[k];

				if (x >= 100 || x < 0 || y >= 100 || y < 0) {
					continue;
				}

				if (vals[x][y] <= vals[i][j]) {
					islow = false;
					break;
				}
			}

			if (islow) {
				lows.pb({i, j});
			}
		}
	}

	vi basins;
	for (pi u : lows) {
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				vis[i][j] = false;
			}
		}
		cur.clear();
		dfs(u.f, u.s);

		basins.pb(sz(cur));
	}

	sort(all(basins), greater<int>());

	ll ans = 1;
	
	for (int i = 0; i < 3; i++) {
		ans *= basins[i];
	}
	cout << ans << "\n";
}