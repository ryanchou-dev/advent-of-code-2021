// pretty standard dijkstra problem today
// im rlly bad at implementing it though
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

void setIO(string name = "") {
	cin.tie(0)->sync_with_stdio(0); // see /general/fast-io
	if (sz(name)) {
		freopen((name + ".in").c_str(), "r", stdin); // see /general/input-output
		freopen((name + ".out").c_str(), "w", stdout);
	}
}

vi dx = {1, 0, -1, 0}, dy = {0, 1, 0, -1};

int dist[500][500], risk[10000][10000];

void dijkstra() {
	priority_queue<array<int, 3>> pq;
	// x, y, cost
	pq.push({0, 0, 0});
	dist[0][0] = 0;

	while (!pq.empty()) {
		array<int, 3> cur = pq.top();
		pq.pop();
		int x = cur[0], y = cur[1], c = cur[2];

		if (c != dist[x][y]) continue;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];

			if (nx < 0 || nx > 99 || ny < 0 || ny > 99) continue;

			if (c + risk[nx][ny] < dist[nx][ny]) {
				dist[nx][ny] = c + risk[nx][ny];
				pq.push({nx, ny, dist[nx][ny]});
			}
		}
	}	

	cout << dist[99][99] << endl;
}
int main() {
	setIO();

	for (int i = 0; i < 100; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 100; j++) {
			risk[i][j] = s.at(j) - '0';
			dist[i][j] = INT32_MAX;
		}
	}
	

	dijkstra();
}