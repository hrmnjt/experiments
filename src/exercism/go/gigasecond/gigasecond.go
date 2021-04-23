/*
Package gigasecond implements a library to return gigasecond post current time
*/
package gigasecond

import "time"

// AddGigasecond prints the 10^9 seconds post current time
func AddGigasecond(t time.Time) time.Time {

	return t.Add(10e8 * time.Second)
}
