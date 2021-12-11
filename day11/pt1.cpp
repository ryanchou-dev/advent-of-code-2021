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

int ans = 0;
vector<vi> inp(10, vector<int>(10, 0));

void increment(int j, int k) {
	if (j >= 10 || k >= 10 || j < 0 || k < 0) {
		return;
	}

	if (inp[j][k] != -1) inp[j][k]++;
}

void check(int j, int k) {
	inp[j][k] = -1;
	ans++;

	increment(j + 1, k);
	increment(j - 1, k);
	increment(j, k + 1);
	increment(j, k - 1);
	increment(j + 1, k + 1);
	increment(j - 1, k - 1);
	increment(j + 1, k - 1);
	increment(j - 1, k + 1);
}
int main() {
	setIO();

	for (int i = 0; i < 10; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 10; j++) {
			inp[i][j] = s.at(j) - '0';
		}
	}

	for (int step = 0; step < 100; step++) {

		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < 10; k++) {
				inp[j][k]++;
			}
		}

		bool stillflashes = true;

		while (stillflashes) {
			stillflashes = false;
			for (int j = 0; j < 10; j++) {
				for (int k = 0; k < 10; k++) {
					if (inp[j][k] > 9) {
						check(j, k);
						stillflashes = true;
					}
				}
			}
		}

		for (int q = 0; q < 10; q++) {
			for (int w = 0; w < 10; w++) {
				if (inp[q][w] == -1) {
					inp[q][w] = 0;
				}
			}
		}
	}
	cout << ans << "\n";
}